
import sys, os
import ast
import fitz
from print import Ui_PrintForm
import OfdtoPdf
from itertools import count
from pathlib import Path
import configparser
# import win32print
from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw
from PySide6.QtGui import QPainter, QPageSize, QPageLayout, QColor, QIntValidator
from PySide6.QtPrintSupport import (
    QPrinter,
    QPrintDialog,
    QPrinterInfo,
    QPrintPreviewDialog,
)
from PySide6.QtCore import (
    QRect,
    QObject,
    QThread,
    Signal,
    QEvent,
    Qt,
    QSizeF,
    QMargins,
    QMarginsF
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QListWidgetItem,
    QFileDialog,
    QStyleFactory,
    QDialogButtonBox,
)


# 第1步：创建一个工作类
class printPdfWorker(QObject):
    finished = Signal()
    progress = Signal(str, str)
    def __init__(self, pdf=None, parent=None):
        super().__init__()
        self.win = parent
        self.paths = pdf
        self.cup = self.win.cup
        self.paper = self.win.paper
        self.printname = self.win.printName
        self.dpi = int(str(self.win.dpi)[:3])
        self.orientation = self.win.dirtion()
        self.pdf_files = []
        ali = self.win.ali
        if "水平居中" in ali:
            self.inter_x = 2
            self.inter_y = 0.5
        elif "靠右居中" in ali:
            self.inter_x = 1
            self.inter_y = 0.5
        elif "垂直两端" in ali:
            self.inter_x = 2
            self.inter_y = 1
        elif ali == "无":
            self.inter_x = 2
            self.inter_y = 0
        self.double = self.win.double
        self._printer = QPrinter(QPrinter.PrinterMode.HighResolution) # 指定了打印机的分辨率模式为高分辨率
        self._printer.setOutputFormat(QPrinter.NativeFormat) # 关键设置 
        self._printer.setPrinterName(self.printname)
        if 'Adobe PDF' in self.printname or 'Microsoft Print to PDF' in self.printname:
            try:
                file_path = self.win.savefile
                self._printer.setOutputFileName(file_path)
            except:
                pass
        self.setprinton()
        


    def setprinton(self):
        if "A4" in self.paper:
            self._printer.setPageSize(QPageSize(QPageSize.A4))
            self.height_dpx, self.width_dpx = self.a4_size(self.dpi, 210, 297)
        elif "A5" in self.paper:
            self._printer.setPageSize(QPageSize(QPageSize.A5))
            self.height_dpx, self.width_dpx = self.a4_size(self.dpi, 148, 210)
        else:
            if "自定义" not in self.paper:
                width, height = map(int, self.paper.split('*'))
                custom_size = QPageSize(QSizeF(width, height), QPageSize.Unit.Millimeter, self.paper, QPageSize.ExactMatch)       
                # 设置打印机的页面尺寸
                self._printer.setPageSize(custom_size)
                 # 关键：禁用系统级纸张匹配 (Qt 5.12+)
                self._printer.setPageLayout(QPageLayout(custom_size, QPageLayout.Portrait, QMarginsF(0, 0, 0, 0), QPageLayout.Millimeter))
                self._printer.pageLayout().setMode(QPageLayout.FullPageMode)  # 禁用驱动裁剪
                 # 计算自定义纸张的像素尺寸
                self.height_dpx, self.width_dpx = self.a4_size(self.dpi, width, height)

        self._printer.setPrintRange(QPrinter.PrintRange.AllPages)
        if self.win.checkbox.isChecked():
            self._printer.setColorMode(QPrinter.ColorMode.GrayScale)
        else:
            self._printer.setColorMode(QPrinter.ColorMode.Color)
        try:
            self._printer.setDuplex(self.double)
        except Exception as e:
            print(e)
        if self.orientation:
            self._printer.setPageOrientation(self.orientation)
        self._printer.setPageMargins(QMargins(2, 2, 2, 2))  # 设置页边距
        # 设置默认打印份数为 1
        self._printer.setCopyCount(self.cup)
        self._printer.setResolution(self.dpi)
        # 3. 使用物理DPI校准
        # physical_dpi = self._printer.physicalDpiX(), self._printer.physicalDpiY()
        # self._printer.setResolution(max(physical_dpi))  # 匹配硬件精度       
        # 修正高 DPI 缩放对预览的影响
        if hasattr(Qt, 'AA_EnableHighDpiScaling'):
            QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    def rundialog(self):
         # 提供了一个标准的打印对话框，允许用户选择打印机、设置打印参数（如打印范围、份数等）
        self.dialog = QPrintDialog(self._printer)
        self.dialog.setOptions(QPrintDialog.PrintToFile | QPrintDialog.PrintSelection)
        if self.dialog.exec():
            self.runprint()
        else:
            self.progress.emit('已取消打印', 'green')
            self.finished.emit()

    def runprint(self, printer=None):
        """长时间运行的打印任务。"""
        try:
            if printer is not None:
                self._printer = printer
            self.setprinton()
            # # 获取打印机DPI 
            # dpi = self._printer.resolution() 
            # print(self._printer.pageLayout().pageSize().name())  # 输出实际生效的纸张类型
            # print(self._printer.pageLayout().pageSize().size(QPageSize.Millimeter))  # 输出尺寸
            # print(dpi)
            if 'A' in self.paper and '版' in self.paper:
                if '两版' in self.paper:
                    num = 2
                elif 'A4六版' in self.paper:
                    num = 6
                elif 'A4三版' in self.paper:
                    num = 3
                elif '四版' in self.paper:
                    num = 4
                if self.win.mergebox.isChecked():
                    images = self.add_image(self.paths)
                    self.A4_sep(images, num)
                else:
                    batch_size = 12
                    for i in range(0, len(self.paths), batch_size):
                        batch_paths = self.paths[i:i + batch_size]
                        images = self.add_image(batch_paths)
                        self.A4_sep(images, num)

            else:
                if self.win.mergebox.isChecked():
                    # 获取打印设备的页面尺寸
                    # page_rect = self._printer.pageRect(QPrinter.DevicePixel)  # 这将返回页面的物理尺寸
                    # print(page_rect)
                    painter = QPainter(self._printer)
                    painter.setRenderHint(QPainter.Antialiasing)
                    # page_rect = page_rect.toRect()  # 转换为QRect对象
                    # painter.setViewport(page_rect)
                    rect = painter.viewport()
                    # rect = painter.viewport()
                    # print(rect)

                    images = self.add_image(self.paths)
                    for pil_image, pageNumber in zip(images, count(1)):

                        if pageNumber > 1:
                            self._printer.newPage() # 通知打印机准备一个新的空白页面
                        self.print_image(pil_image, rect, painter)


                    # 清理
                    painter.end()

                else:

                    for index, path in enumerate(self.paths):
                        painter = QPainter(self._printer)
                        # painter.setViewport(QRect(0, 0, self.width_dpx, self.height_dpx))
                        rect = painter.viewport()
                        images = []
                        path = Path(path)
                        suffix = path.suffix.lower()
                        if suffix == '.pdf':
                            images = self.open_pdf(path, images)
                            for pil_image, pageNumber in zip(images, count(1)):
                                if pageNumber > 1:
                                    self._printer.newPage() # 通知打印机准备一个新的空白页面
                                self.print_image(pil_image, rect, painter)
                        elif suffix == '.ofd':
                            path, self.pdf_files = OfdtoPdf.ofd_to_pdf(str(path), self.pdf_files)
                            images = self.open_pdf(path, images)
                            for pil_image, pageNumber in zip(images, count(1)):
                                if pageNumber > 1:
                                    self._printer.newPage() # 通知打印机准备一个新的空白页面
                                self.print_image(pil_image, rect, painter)
                        else:
                            with Image.open(path) as image:
                                pil_image = image.copy()
                                self.print_image(pil_image, rect, painter)
                        # self.progress.emit(index+1, len(self.paths))
                        # 清理
                        painter.end()

            self.progress.emit('文件已发送至打印机', 'green')
        except Exception as e:
            print(f'打印出错{e}')
        finally:
            if self.pdf_files:
                OfdtoPdf.remove_pdf(self.pdf_files)
                self.pdf_files = []
            # del self._printer
            self.finished.emit()

    def open_pdf(self, path, images):
        with fitz.open(path) as pdf:
            # n_pages = len(pdf)
            # printRange=[]

            # fromPage = self._printer.fromPage()
            # toPage = self._printer.toPage()
            # printRange = range(n_pages) if fromPage == 0 else range(fromPage-1, toPage)
            # page_indices = [i for i in printRange]

            num_pages = len(pdf)
            printRange = range(num_pages)
            page_indices = [i for i in printRange]

            for index in page_indices:
                pixmap = pdf[index].get_pixmap(dpi=self.dpi)
                # 将像素图转换为 PIL 图像对象
                pil_image=Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
                images.append(pil_image)
        return images

    def add_image(self, paths=None):
        images = []
        file_paths = paths
        # file_paths = [path for path in file_paths if path.endswith('.pdf')] + \
        #            [path for path in file_paths if path.endswith(('.jpg', '.jpeg', '.png'))]
        if self.win.repeat.isChecked():
            # 将路径重复一次
            file_paths = [path for path in file_paths for _ in range(2)]
        for index, path in enumerate(file_paths):
            path = Path(path)
            suffix = path.suffix.lower()
            if suffix == '.pdf':
                images = self.open_pdf(path, images)
            elif suffix == '.ofd':
                path, self.pdf_files = OfdtoPdf.ofd_to_pdf(str(path), self.pdf_files)
                images = self.open_pdf(path, images)
            else:
                with Image.open(path) as image:
                    images.append(image.copy())
        return images


    def A4_sep(self, images, batch_size):
        painter = QPainter(self._printer)
        for i, pageNumber in zip(range(0, len(images), batch_size), count(1)):
            batch_paths = images[i:i + batch_size]
            if pageNumber > 1:
                self._printer.newPage()

            # 根据 batch_size 调用不同的拼接函数
            if batch_size == 6:
                self.join_pic6(batch_paths, painter)
            elif batch_size == 4:
                self.join_pic4(batch_paths, painter)
            elif batch_size == 3:
                self.join_pic3(batch_paths, painter)
            elif batch_size == 2:
                self.join_pic(batch_paths, painter)
            else:
                raise ValueError("不支持的方法")

        # 清理
        painter.end()


    def print_image(self, pil_image, rect, painter):
        # 计算图像和视口的宽高比，并根据需要旋转图像
        pilWidth, pilHeight = pil_image.size
        imageRatio = pilHeight/pilWidth # 计算宽高比
        viewportRatio= rect.height()/rect.width()   # 获取视口的宽高比
        A4Ratio = self.height_dpx/self.width_dpx
        # print(pil_image.size,rect.width(),rect.height(),self.width_dpx,self.height_dpx)

        if self.win.up == "自动旋转":
            # 如果方向与打印格式方向不一致，则旋转图像
            if (A4Ratio < 1 and imageRatio > 1) or (A4Ratio > 1 and imageRatio < 1):
                pil_image = pil_image.transpose(Image.ROTATE_270)
                pilWidth, pilHeight = pil_image.size
                imageRatio = pilHeight/pilWidth

            # 计算缩放比例
            scale = min(rect.width() / pilWidth, rect.height() / pilHeight)
            scaledWidth = int(pilWidth * scale)
            scaledHeight = int(pilHeight * scale)
            if A4Ratio < 1:
                # 计算偏移量
                xOffset = int((rect.width() - scaledWidth) / self.inter_x)
                yOffset = int((rect.height() - scaledHeight) / 2)
            else:
                xOffset = int((rect.width() - scaledWidth) / 2)
                yOffset = int((rect.height() - scaledHeight) / self.inter_x)
        else:
            # 计算缩放比例
            scale = min(rect.width() / pilWidth, rect.height() / pilHeight)
            scaledWidth = int(pilWidth * scale)
            scaledHeight = int(pilHeight * scale)
            # 计算偏移量
            xOffset = int((rect.width() - scaledWidth) / self.inter_x)
            yOffset = int((rect.height() - scaledHeight) * self.inter_y)

        # print(pil_image.size,rect.width(),rect.height(),self.width_dpx,self.height_dpx)
        # 调整绘图区域以适应可用视口
        if viewportRatio > imageRatio:  # 如果视口宽高比大于图像宽高比，调整高度以适应图像5：6> 4:6  6/(6/4)=  4 : 6
            y=int(rect.width()/(pilWidth/pilHeight))
            printArea=QRect(xOffset,yOffset,rect.width(),y)
        else:
            x = int(pilWidth/pilHeight*rect.height())
            printArea=QRect(xOffset,yOffset,x,rect.height())

        # printArea=QRect(xOffset,yOffset,rect.width(),rect.height())
        image = ImageQt(pil_image)
        # 打印图像
        painter.drawImage(printArea, image) # 在计算好的绘图区域绘制图像
        # firstPage = False
        return painter

    def join_pic(self, image_list, painter):
        # 计算每行每列放置图片的数量
        cell_width = int(self.width_dpx)
        cell_height = int(self.height_dpx / 2)
        # 确保传入的图片列表有6张图片
        if len(image_list) < 2:
            for n in range(len(image_list),2):
                image  = Image.new('RGB', (cell_width, cell_height) ,'white')
                image_list.append(image)

        # 对每张图片进行预处理，如旋转保证宽高比合适、调整大小适应A4纸布局
        processed_images = []
        for image in image_list:
            pilWidth, pilHeight = image.size
            imageRatio = pilHeight / pilWidth
            if imageRatio > 1:
                image = image.transpose(Image.ROTATE_90)
            zoom = 0.97
            width = int(cell_width*zoom)
            height = int(cell_height*zoom)
            # 调整图片大小
            processed_image = self.resize_image(image, width, height)
            processed_images.append(processed_image)

        # 竖向拼接两张图片
        merged_image = Image.new('RGB', (self.width_dpx , self.height_dpx), 'white')
        for index, img in enumerate(processed_images):
            row = index % 2
            col = 0
            add_y = self.inter_y * row if self.inter_y == 1 else self.inter_y
            x = int(col * cell_width + int((cell_width - img.size[0]) / self.inter_x))
            y = int(row * cell_height + int((cell_height - img.size[1]) * add_y))
            merged_image.paste(img, (x, y))
        if self.win.line.isChecked():
            draw = ImageDraw.Draw(merged_image)
            width = int(self.width_dpx/6)
            # 绘制水平裁切线（同样红色，线宽为2像素）
            draw.line([(0, cell_height), (width, cell_height)], fill="red", width=1)
            draw.line([(self.width_dpx-width, cell_height), (self.width_dpx, cell_height)], fill="red", width=1)
        rect = painter.viewport()
        self.print_image(merged_image, rect, painter)

    def join_pic6(self, image_list, painter):
        """
        将传入的图片列表中的6张图片绘制在一张A4纸上。
        """
        # 计算每行每列放置图片的数量
        cell_width = int(self.width_dpx / 2)
        cell_height = int(self.height_dpx / 3)
        # 确保传入的图片列表有6张图片
        if len(image_list) < 6:
            for n in range(len(image_list),6):
                image  = Image.new('RGB', (cell_width, cell_height) ,'white')
                image_list.append(image)
        # 对每张图片进行预处理，如旋转保证宽高比合适、调整大小适应A4纸布局
        processed_images = []
        for image in image_list:
            pilWidth, pilHeight = image.size
            imageRatio = pilHeight / pilWidth
            if imageRatio > 1:
                image = image.transpose(Image.ROTATE_90)
            zoom = 0.97
            width = int(cell_width*zoom)
            height = int(cell_height*zoom)
            # 调整图片大小
            processed_image = self.resize_image(image, width, height)
            processed_images.append(processed_image)


        # 创建空白的A4纸大小的图片用于合并
        merged_image = Image.new('RGB', (self.width_dpx, self.height_dpx), 'white')

        # 循环将处理好的图片按布局粘贴到合并图片上
        for index, img in enumerate(processed_images):
            row = index // 2
            col = index % 2
            add_y = self.inter_y * row/2 if self.inter_y == 1 else self.inter_y
            x = int(col * cell_width + int((cell_width - img.size[0]) / self.inter_x))
            y = int(row * cell_height + int((cell_height - img.size[1]) * add_y))
            merged_image.paste(img, (x, y))
        if self.win.line.isChecked():
            draw = ImageDraw.Draw(merged_image)
            draw.line([(cell_width, 0), (cell_width, self.height_dpx)], fill="red", width=1)
            # 绘制水平裁切线（同样红色，线宽为2像素）
            draw.line([(0, cell_height), (self.width_dpx, cell_height)], fill="red", width=1)
            draw.line([(0, cell_height*2), (self.width_dpx, cell_height*2)], fill="red", width=1)
        rect = painter.viewport()
        self.print_image(merged_image, rect, painter)

    def join_pic4(self, image_list, painter):
        """
        将传入的图片列表中的图片绘制在一张A4纸上。
        """
        # 计算每行每列放置图片的数量
        cell_width = int(self.width_dpx / 2)
        cell_height = int(self.height_dpx / 2)

        # 确保传入的图片列表有4张图片
        if len(image_list) < 4:
            for n in range(len(image_list),4):
                image  = Image.new('RGB', (cell_width, cell_height) ,'white')
                image_list.append(image)
        # 对每张图片进行预处理，如旋转保证宽高比合适、调整大小适应A4纸布局
        processed_images = []
        for image in image_list:
            pilWidth, pilHeight = image.size
            imageRatio = pilHeight / pilWidth
            if imageRatio < 1:
                image = image.transpose(Image.ROTATE_270)
            zoom = 0.97
            width = int(cell_width*zoom)
            height = int(cell_height*zoom)
            # 调整图片大小
            processed_image = self.resize_image(image, width, height)
            processed_images.append(processed_image)


        # 创建空白的A4纸大小的图片用于合并
        merged_image = Image.new('RGB', (self.width_dpx, self.height_dpx), 'white')

        # 循环将处理好的图片按布局粘贴到合并图片上
        for index, img in enumerate(processed_images):
            row = index // 2
            col = index % 2
            add_y = self.inter_y * row if self.inter_y == 1 else self.inter_y
            x = int(col * cell_width + int((cell_width - img.size[0])/self.inter_x))
            y = int(row * cell_height + int((cell_height - img.size[1]) * add_y))
            merged_image.paste(img, (x, y))
        if self.win.line.isChecked():
            draw = ImageDraw.Draw(merged_image)

            draw.line([(cell_width, 0), (cell_width, self.height_dpx)], fill="red", width=1)

            # 绘制水平裁切线（同样红色，线宽为2像素）
            draw.line([(0, cell_height), (self.width_dpx, cell_height)], fill="red", width=1)

        rect = painter.viewport()
        self.print_image(merged_image, rect, painter)

    def join_pic3(self, image_list, painter):
        """
        将传入的图片列表中的图片绘制在一张A4纸上。
        """
        # 计算每行每列放置图片的数量
        cell_width = int(self.width_dpx / 1)
        cell_height = int(self.height_dpx / 3)

        # 确保传入的图片列表有4张图片
        if len(image_list) < 3:
            for n in range(len(image_list),3):
                image  = Image.new('RGB', (cell_width, cell_height) ,'white')
                image_list.append(image)
        # 对每张图片进行预处理，如旋转保证宽高比合适、调整大小适应A4纸布局
        processed_images = []
        for image in image_list:
            pilWidth, pilHeight = image.size
            imageRatio = pilHeight / pilWidth
            if imageRatio > 1:
                image = image.transpose(Image.ROTATE_90)
            zoom = 0.97
            width = int(cell_width*zoom)
            height = int(cell_height*zoom)
            # 调整图片大小
            processed_image = self.resize_image(image, width, height)
            processed_images.append(processed_image)


        # 创建空白的A4纸大小的图片用于合并
        merged_image = Image.new('RGB', (self.width_dpx, self.height_dpx), 'white')

        # 循环将处理好的图片按布局粘贴到合并图片上
        for index, img in enumerate(processed_images):
            row = index % 3
            col = 0
            add_y = self.inter_y * row/2 if self.inter_y == 1 else self.inter_y
            x = int(col * cell_width + int((cell_width - img.size[0]) /self.inter_x))
            y = int(row * cell_height + int((cell_height - img.size[1]) * add_y))
            merged_image.paste(img, (x, y))
        if self.win.line.isChecked():
            draw = ImageDraw.Draw(merged_image)

            draw.line([(cell_width, 0), (cell_width, self.height_dpx)], fill="red", width=1)

            # 绘制水平裁切线（同样红色，线宽为2像素）
            draw.line([(0, cell_height), (self.width_dpx, cell_height)], fill="red", width=1)
            draw.line([(0, cell_height*2), (self.width_dpx, cell_height*2)], fill="red", width=1)

        rect = painter.viewport()
        self.print_image(merged_image, rect, painter)

    def resize_image(self, image, cell_width, cell_height):
            """
            根据A4纸尺寸相关属性，按比例调整图片大小，使其适应单个单元格布局。
            参数:
            image: 要调整大小的图片对象。
            返回:
            调整好大小的图片对象。
            """
            # 保持图片比例，调整图片大小
            ratio = int(cell_height) / image.size[1]
            max_width = int(image.size[0] * ratio)
            max_height = int(cell_height)
            if max_width > cell_width:
                max_width = cell_width
                ratio = cell_width / image.size[0]
                max_height = int(image.size[1] * ratio)
            new_width = max_width
            new_height = max_height
            # 调整图片大小
            resized_image = image.resize((new_width, new_height))
            return resized_image

    def a4_size(self, dpi, width, height):
        # 将A4纸的物理尺寸转换为英寸
        a4_width= width / 25.4
        a4_height = height / 25.4
        # 根据DPI计算A4纸一半的高度（像素）
        height_dpx = int(a4_height * dpi)
        width_dpx = int(a4_width * dpi)
        return height_dpx, width_dpx


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_PrintForm()
        self.ui_win = self.windowFlags()
        self.ui.setupUi(self)
        self.longRunningBtn = self.ui.pushButton
        self.longRunningBtn.clicked.connect(self.runPrintTask)

        self.addfile = self.ui.pushButton_2
        self.addfile.clicked.connect(self.getFile)

        self.clearfile = self.ui.pushButton_3
        self.clearfile.clicked.connect(self.clearFile)

        self.sysPrint = self.ui.toolButton
        self.sysPrint.clicked.connect(self.rundio)

        self.yulanBtn = self.ui.pushButton_4
        self.yulanBtn.clicked.connect(self.preview)
        self.spinbox = self.ui.doubleSpinBox
        self.paper_box = self.ui.comboBox
        self.dpi_box = self.ui.comboBox_2
        self.double_box = self.ui.comboBox_3
        self.alignment = self.ui.comboBox_4
        self.direction = self.ui.comboBox_6
        self.paper_box.activated.connect(self.setdirection)
        self.bar = self.ui.label_8
        self.ui.buttonBox.accepted.connect(self.send_number)
        self.listwidget = self.ui.listWidget
        self.checkbox = self.ui.checkBox
        self.mergebox = self.ui.checkBox_2
        self.line = self.ui.checkBox_3
        self.repeat = self.ui.checkBox_4
        self.printbox = self.ui.comboBox_5
        self.load_printers()
        self.small_win = self.ui.dockWidget
        self.small_win.hide()
        self.input_win = self.ui.dockWidget_2
        self.input_win.hide()
        self.textbox = self.ui.textEdit
        self.textbox.textChanged.connect(self.changedText)
        self.load_config()
        self.setdirection()
        self.file_path = []
        # 安装事件过滤器
        self.listwidget.viewport().installEventFilter(self)
        self.listwidget.keyPressEvent = self.on_key_press  # 绑定键盘事件处理函数

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonDblClick and source is self.listwidget.viewport():
            # 捕获双击事件
            self.small_win.show()
            return True
        return super().eventFilter(source, event)

    def setdirection(self):
        if "版" in self.paper_box.currentText():
            self.direction.setCurrentIndex(0)
            self.direction.setEnabled(False)
        else:
            self.direction.setEnabled(True)
        if self.paper_box.currentText() == "自定义纸张":
            self.input_win.show()
            self.zdy_width = self.ui.lineEdit
            self.zdy_hight = self.ui.lineEdit_2
            # 创建一个 QIntValidator，限制输入为整数
            validator = QIntValidator(self)
            self.zdy_width.setValidator(validator)
            self.zdy_hight.setValidator(validator)


    def changedText(self):
        self.clearFile()
        # 获取文本并按行分割
        text = self.textbox.toPlainText()
        lines = text.splitlines()
        # 将每一行添加到 QListWidget
        for line in lines:
            if line.strip():  # 只添加非空行
                self.showListwidget(line)

    def send_number(self):
        width = self.zdy_width.text()
        hight = self.zdy_hight.text()
        if width and hight:
            # 组合用户输入的内容
            combined_text = f'{width} * {hight}'
            # 获取当前选项的总数
            item_count = self.paper_box.count()
            # 检查是否达到最大选项数量
            if item_count >= self.paper_box.maxCount():
                # 删除第8个选项
                self.paper_box.removeItem(item_count-3)
                item_count = self.paper_box.count()

            self.paper_box.addItem(combined_text)
            # 设置当前选中项为新添加的内容
            self.paper_box.setCurrentIndex(item_count)
        else:
            # 如果用户没有输入内容，恢复之前的选项
            self.paper_box.setCurrentIndex(0)
        self.input_win.close()

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('printConfig.ini')  # 读取配置文件
        self.spinbox.setValue(int(config.get('Print', 'Series', fallback=1)))

        self.dpi_box.setCurrentIndex(int(config.get('Print', 'Dpi', fallback=1)))
        self.double_box.setCurrentIndex(int(config.get('Print', 'Double', fallback=0)))
        self.alignment.setCurrentIndex(int(config.get('Print', 'Center', fallback=0)))
        self.printbox.setCurrentText(config.get('Print', 'PrintName', fallback=''))
        self.direction.setCurrentIndex(int(config.get('Print', 'PageDirection', fallback=0)))
        self.checkbox.setCheckState(Qt.CheckState.Checked if config.getboolean('Print', 'Color', fallback=False) else Qt.CheckState.Unchecked)
        self.mergebox.setCheckState(Qt.CheckState.Checked if config.getboolean('Print', 'Mergebox', fallback=False) else Qt.CheckState.Unchecked)
        self.line.setCheckState(Qt.CheckState.Checked if config.getboolean('Print', 'Line', fallback=False) else Qt.CheckState.Unchecked)
        self.repeat.setCheckState(Qt.CheckState.Checked if config.getboolean('Print', 'Repeat', fallback=False) else Qt.CheckState.Unchecked)
        last_three_items = config.get('Print', 'LastThreeItems',fallback='[]')
        for item in ast.literal_eval(last_three_items):
            self.paper_box.addItem(item)
        self.paper_box.setCurrentIndex(int(config.get('Print', 'Paper', fallback=0)))

    def doublePrint(self):
        double = self.double_box.currentIndex()
        if double == 0:
            return QPrinter.DuplexMode.DuplexNone
        elif double == 1:
            return QPrinter.DuplexLongSide
        elif double == 2:
            return QPrinter.DuplexShortSide
        elif double == 3:
            return QPrinter.DuplexAuto

    def dirtion(self):
        self.up = self.direction.currentText()
        # if self.up == "纵向":
        #     return QPageLayout.Portrait
        if self.up == "横向":
            return QPageLayout.Landscape
        else:
            return QPageLayout.Portrait

    def clearFile(self):
        self.file_path = []
        self.listwidget.clear()
        self.runBar('准备就绪......','black')

    def getFile(self):
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='选择文件',
            filter='文件类型 (*.pdf *.jpg *.png *.jpeg *.bmp *.ofd);;Images (*.png *.jpg *.jpeg *.bmp);;PDF Files (*.pdf);;OFD Files (*.ofd)'
        )
        if response:
            file_paths = response[0]
            for path in file_paths:
                self.showListwidget(path)

    def showListwidget(self, path):
        self.file_path.append(path)
        item_widget = QListWidgetItem(path)
        self.listwidget.addItem(item_widget)
        self.bar.setText(f'已添加文件:{len(self.file_path)}个')
        return self.file_path
    
    def on_key_press(self, event):
        if event.key() == Qt.Key_Delete:
            # 获取当前选中的列表项
            current_item = self.listwidget.currentItem()
            if current_item:
                # 从self.file_path中删除对应的路径
                self.file_path.remove(current_item.text())
                # 从列表控件中删除选中的项
                self.listwidget.takeItem(self.listwidget.row(current_item))
                # 更新状态栏信息
                self.bar.setText(f'待打印文件:{len(self.file_path)}个')

    def lianjie(self, paths):
        self.clearFile()
        valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.pdf', '.ofd'}
        for path in paths:
            _, extensions= os.path.splitext(path)
            if extensions.lower() in valid_extensions:
                self.showListwidget(path)

    def load_printers(self):
        # 获取所有打印机的名称
        printers = QPrinterInfo.availablePrinters()
        printer_names = [printer.printerName() for printer in printers]  # 获取打印机名称
        self.printbox.addItems(printer_names)  # 将打印机名称添加到 QComboBox

    def printdata(self):
        self.cup = self.spinbox.value()
        self.paper = self.paper_box.currentText()
        self.dpi = self.dpi_box.currentText()
        self.ali = self.alignment.currentText()
        self.double = self.doublePrint()
        self.printName = self.printbox.currentText()
        self.runBar('正在发送页面到打印机\n请勿关闭程序...','red')

    def rundio(self):
        # 第1步：
        pdf_file = self.file_path
        if not pdf_file:
            self.runBar('没有待打印的文件','blue')
            return
        self.printdata()
        # # 第2步：创建一个QThread对象
        # self.thread = QThread()
        # # 第3步：创建一个工作对象
        # self.worker = printPdfWorker(pdf_file, self)
        # # 第4步：将工作对象移到线程
        # self.worker.moveToThread(self.thread)
        # # 第5步：连接信号和槽
        # self.thread.started.connect(self.worker.rundialog)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.worker.progress.connect(self.runBar)
        # # 第6步：启动线程
        # self.thread.start()
        self.worker = printPdfWorker(pdf_file, self)
        self.worker.rundialog()
        self.worker.finished.connect(self.worker.deleteLater)
        self.runBar('文件已发送至打印机', 'green')

    def runPrintTask(self):
        # 第1步：
        pdf_file = self.file_path
        if not pdf_file:
            self.runBar('没有待打印的文件','blue')
            return
        self.printdata()
        if 'Adobe PDF' in self.printName or 'Microsoft Print to PDF' in self.printName:
            self.savefile = QFileDialog.getSaveFileName(self, "保存PDF文件", "document.pdf", "PDF Files (*.pdf)")[0]
        # 第2步：创建一个QThread对象
        self.thread = QThread()
        # 第3步：创建一个工作对象
        self.worker = printPdfWorker(pdf_file, self)
        # 第4步：将工作对象移到线程
        self.worker.moveToThread(self.thread)
        # 第5步：连接信号和槽
        self.thread.started.connect(self.worker.runprint)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.progress.connect(self.runBar)
        self.thread.finished.connect(self.thread.deleteLater)
        # 第6步：启动线程
        self.thread.start()

    def preview(self):
        # 第1步：
        pdf_file = self.file_path
        if not pdf_file:
            self.runBar('没有待打印的文件','blue')
            return
        self.printdata()
         # 强制刷新界面
        QApplication.processEvents()
        self.worker3 = printPdfWorker(pdf_file, self)
        self.worker3.progress.connect(self.runBar)
        preview_dialog = QPrintPreviewDialog(self)
        preview_dialog.paintRequested.connect(self.worker3.runprint)
        # 设置预览框标题
        preview_dialog.setWindowTitle("打印预览")
        # 设置预览框大小
        preview_dialog.resize(800, 600)
        preview_dialog.exec()

    def runBar(self, text, color='black'):
        palette = self.bar.palette()
        palette.setColor(self.bar.foregroundRole(), QColor(color))
        self.bar.setPalette(palette)
        self.bar.setText(text)

    def dragEnterEvent(self, event):
        # 如果拖放的 MIME 数据包含 URL（通常是文件路径）
        if event.mimeData().hasUrls():
            # 接受拖放事件
            event.accept()
        else:
            # 否则忽略拖放事件
            event.ignore()

    def dropEvent(self, event):
        valid_extensions = {'.png', '.jpg', '.jpeg', '.pdf', '.bmp', '.ofd'}
        dropped_files = []
        # 遍历拖放的 URL 列表
        for url in event.mimeData().urls():
            # 获取 URL 对应的本地文件路径
            file_path = url.toLocalFile()
            if os.path.isdir(file_path):
                # 如果是文件夹，遍历文件夹下的所有文件
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        full_file_path = os.path.join(root, file)
                        _, extension = os.path.splitext(full_file_path)
                        if extension.lower() in valid_extensions:
                            dropped_files.append(full_file_path)
            else:
                _, extension = os.path.splitext(file_path)
                if extension.lower() in valid_extensions:
                    dropped_files.append(file_path)
        for file_path in dropped_files:
            self.showListwidget(file_path)

    def closeEvent(self, event):
        self.save_combobox()
        event.accept()

    def save_combobox(self):
        config = configparser.ConfigParser()
        config.read('printConfig.ini')  # 读取配置文件
        # 检查是否有一个section来保存组合框的状态
        if 'Print' not in config:
            config.add_section('Print')
        # 获取当前选中的索引
        cup = self.spinbox.value()
        paper = self.paper_box.currentIndex()
        dpi = self.dpi_box.currentIndex()
        double = self.double_box.currentIndex()
        center = self.alignment.currentIndex()
        printName = self.printbox.currentText()
        direction =  self.direction.currentIndex()
        mergebox = int(self.mergebox.checkState() == Qt.CheckState.Checked)
        line = int(self.line.checkState() == Qt.CheckState.Checked)
        repeat = int(self.repeat.checkState() == Qt.CheckState.Checked)
        lastoption = []
        item_count = self.paper_box.count()
        if item_count > self.paper_box.maxCount()-3:
            for i in range(self.paper_box.maxCount()-3, item_count):
                lastoption.append(self.paper_box.itemText(i))
        # 保存选中的索引
        config['Print'] = {'Series': int(cup),
                           'Paper': str(paper),
                           'Dpi': str(dpi),
                           'Double': str(double),
                           'Center': str(center),
                           'Color':str(int(self.checkbox.checkState() == Qt.CheckState.Checked)),
                           'PrintName':str(printName),
                           'PageDirection': str(direction),
                           'Mergebox': str(mergebox),
                           'Line': str(line),
                           'Repeat': str(repeat),
                           'LastThreeItems': lastoption,
                           }

        # 将更新后的配置写回到文件
        with open('printConfig.ini', 'w') as configfile:
            config.write(configfile)


