from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFrame
import os
import sys
import time

class ProcessingThread(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)

    def __init__(self, text, initial_key, iterations):
        super().__init__()
        self.text = text
        self.initial_key = initial_key
        self.iterations = iterations

    def run(self):
        processed_text = process_text(self.text, self.initial_key, self.iterations)
        self.finished.emit(processed_text)

class Loading_Window(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(359, 184)
        Frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 341, 51))
        self.label.setStyleSheet("font: 75 25pt \"Tahoma\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 215, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Loading..."))
        self.label.setText(_translate("Frame", "Proceessing..."))

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(836, 572)
        Frame.setMinimumSize(QtCore.QSize(500, 500))
        Frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.title = QtWidgets.QLabel(Frame)
        self.title.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.title.setStyleSheet("font: 26pt \"Showcard Gothic\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 215, 0);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.logTxt = QtWidgets.QTextBrowser(Frame)
        self.logTxt.setGeometry(QtCore.QRect(500, 320, 321, 241))
        self.logTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
# "font: 12pt \"Arial\";\n"
# "font: 12pt \"MS Shell Dlg 2\";\n"
# "font: 12pt \"MS UI Gothic\";\n"
# "font: 12pt \"Arial Unicode MS\";\n"
# "font: 12pt \"SimSun\";\n"
"background-color: rgb(212, 212, 212);")
        self.logTxt.setObjectName("logTxt")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(520, 290, 271, 31))
        self.label_3.setMaximumSize(QtCore.QSize(271, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.fileBtn = QtWidgets.QPushButton(Frame)
        self.fileBtn.setGeometry(QtCore.QRect(360, 70, 81, 31))
        self.fileBtn.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"font: 12pt \"Tahoma\";")
        self.fileBtn.setObjectName("fileBtn")
        self.processBtn = QtWidgets.QPushButton(Frame)
        self.processBtn.setGeometry(QtCore.QRect(530, 160, 131, 31))
        self.processBtn.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"font: 12pt \"Tahoma\";")
        self.processBtn.setObjectName("processBtn")
        self.status = QtWidgets.QLabel(Frame)
        self.status.setGeometry(QtCore.QRect(500, 240, 321, 31))
        self.status.setStyleSheet("font: 12pt \"Tahoma\";\n"
"background-color: rgb(212, 212, 212);")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.outputTxt = QtWidgets.QTextBrowser(Frame)
        self.outputTxt.setGeometry(QtCore.QRect(10, 370, 471, 191))
        self.outputTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
# "font: 12pt \"Arial\";\n"
# "font: 12pt \"MS Shell Dlg 2\";\n"
# "font: 12pt \"MS UI Gothic\";\n"
# "font: 12pt \"Arial Unicode MS\";\n"
# "font: 12pt \"SimSun\";\n"
"background-color: rgb(212, 212, 212);")
        self.outputTxt.setObjectName("outputTxt")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 81, 31))
        self.label_5.setStyleSheet("font: 12pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 81, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_6.setObjectName("label_6")
        self.pathTxt = QtWidgets.QLineEdit(Frame)
        self.pathTxt.setGeometry(QtCore.QRect(100, 70, 251, 31))
        self.pathTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
"background-color: rgb(212, 212, 212);")
        self.pathTxt.setText("")
        self.pathTxt.setObjectName("pathTxt")
        self.keyTxt = QtWidgets.QLineEdit(Frame)
        self.keyTxt.setGeometry(QtCore.QRect(510, 70, 141, 31))
        self.keyTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
"background-color: rgb(212, 212, 212);")
        self.keyTxt.setText("")
        self.keyTxt.setMaxLength(10)
        self.keyTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.keyTxt.setObjectName("keyTxt")
        self.cycleTxt = QtWidgets.QLineEdit(Frame)
        self.cycleTxt.setGeometry(QtCore.QRect(710, 70, 111, 31))
        self.cycleTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
"background-color: rgb(212, 212, 212);")
        self.cycleTxt.setText("")
        self.cycleTxt.setMaxLength(4)
        self.cycleTxt.setObjectName("cycleTxt")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(470, 70, 31, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(660, 70, 41, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(490, 100, 141, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.inputTxt = QtWidgets.QTextEdit(Frame)
        self.inputTxt.setGeometry(QtCore.QRect(10, 150, 471, 191))
        self.inputTxt.setStyleSheet("font: 12pt \"Tahoma\";\n"
# "font: 12pt \"Arial\";\n"
# "font: 12pt \"MS Shell Dlg 2\";\n"
# "font: 12pt \"MS UI Gothic\";\n"
# "font: 12pt \"Arial Unicode MS\";\n"
# "font: 12pt \"SimSun\";\n"
"background-color: rgb(212, 212, 212);")
        self.inputTxt.setObjectName("inputTxt")
        self.resetBtn = QtWidgets.QPushButton(Frame)
        self.resetBtn.setGeometry(QtCore.QRect(670, 160, 131, 31))
        self.resetBtn.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"font: 12pt \"Tahoma\";")
        self.resetBtn.setObjectName("resetBtn")
        self.label_9 = QtWidgets.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(520, 210, 271, 31))
        self.label_9.setMaximumSize(QtCore.QSize(271, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"Tahoma\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        
        self.fileBtn.clicked.connect(self.open_file)
        self.processBtn.clicked.connect(self.process)
        self.resetBtn.clicked.connect(self.reset_inputs)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Cryptographic"))
        self.title.setText(_translate("Frame", "Cryptographic"))
        self.logTxt.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Tahoma\';\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Frame", "Select file: "))
        self.label_3.setText(_translate("Frame", "Keys Generated"))
        self.fileBtn.setText(_translate("Frame", "Browse"))
        self.processBtn.setText(_translate("Frame", "Start Process"))
        self.status.setText(_translate("Frame", "---"))
        self.outputTxt.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("Frame", "Output: "))
        self.label_6.setText(_translate("Frame", "Data Input:"))
        self.label_4.setText(_translate("Frame", "Key:"))
        self.label_7.setText(_translate("Frame", "Cycle:"))
        self.label_8.setText(_translate("Frame", "(Binary)"))
        self.resetBtn.setText(_translate("Frame", "Reset"))
        self.label_9.setText(_translate("Frame", "Status"))

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Text Files (*.txt)")
        if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                        data = file.read()
                        self.inputTxt.setText(data)
                        self.pathTxt.setText(file_path)
                        # clear other text before
                        self.keyTxt.clear()
                        self.cycleTxt.clear()
                        self.outputTxt.clear()
                        self.logTxt.clear()
                        self.status.clear()
                        # self.processTxt.clear()

    def process(self):
        print('Processing...')
        self.outputTxt.clear()
        self.logTxt.clear()
        PATH = self.pathTxt.text()
        INPUT_DATA = self.inputTxt.toPlainText()
        INITIAL_KEY = self.keyTxt.text()
        ITERATION = self.cycleTxt.text()
        
        if INPUT_DATA == '':
                self.status.setText("Select file or input data...")
        elif not os.path.exists(PATH) and INPUT_DATA == '':
                self.status.setText("Invalid file path")
        elif INITIAL_KEY == '' or not INITIAL_KEY.isdigit() or int(INITIAL_KEY) <= 0:
                self.status.setText("Input value in key...")
        elif not is_binary(INITIAL_KEY):
                self.status.setText("Initial key must be binary")
        elif ITERATION == '':
                self.status.setText("Input value in cycle...")
        elif int(ITERATION) < 1:
                self.status.setText("Cycle value must be greater than 0...")
        else:
                self.clear_inputs()
                # Show loading window
                loading_window = Loading_Window() 
                loading_frame = QFrame()  
                loading_window.setupUi(loading_frame)  
                loading_frame.show()

                text = self.inputTxt.toPlainText()
                encrypted_text = process_text(text, INITIAL_KEY, int(ITERATION))
                # print(f'Encrypted text: {encrypted_text}')

                # Display logs
                self.display_txt(encrypted_text)

                # Get the directory path of the current script
                script_directory = os.path.dirname(__file__)

                # Construct the save path for the encrypted file in the root directory
                encrypted_file_name = f"processed_data.txt"
                save_path = os.path.join(script_directory, encrypted_file_name)

                # Save the encrypted text to the file in the root directory
                with open(save_path, 'w', encoding='utf-8') as save_file:
                        save_file.write(encrypted_text)

                self.status.setText("Process Complete")

                # Close loading window when processing is done
                loading_frame.close()

    def display_txt(self, encrypted_text):
        global key_logs
        global process_logs

        self.logTxt.setText('\n'.join(key_logs))
        self.outputTxt.setText(encrypted_text)
        print('\n'.join(process_logs)) 
        
        print("Text displayed successfully!")
        print(key_logs[0])
        print(process_logs[0])
        key_logs = []
        process_logs = []

    def clear_inputs(self):
        self.outputTxt.clear()
        self.logTxt.clear()
        self.status.clear()
        # self.processTxt.clear()

    def reset_inputs(self):
        self.pathTxt.clear()
        self.keyTxt.clear()
        self.cycleTxt.clear()
        self.logTxt.clear()
        self.inputTxt.clear()
        self.outputTxt.clear()
        self.status.clear()
        # self.processTxt.clear()

# ----------------------Cryptographic Functions-------------------------------------------------------

# Define the function to apply Rule 30 of the cellular automaton
def apply_rule30(cell, left, right):
        # Define the rules for the cellular automaton
        if left == '1' and cell == '1' and right == '1':
                return '0'
        elif left == '1' and cell == '1' and right == '0':
                return '0'
        elif left == '1' and cell == '0' and right == '1':
                return '0'
        elif left == '1' and cell == '0' and right == '0':
                return '1'
        elif left == '0' and cell == '1' and right == '1':
                return '1'
        elif left == '0' and cell == '1' and right == '0':
                return '1'
        elif left == '0' and cell == '0' and right == '1':
                return '1'
        else:
                return '0'

# Generate the next generation of keys using Rule 30
def generate_next_generation(cells):
        next_gen = ''
        for i in range(len(cells)):
                left = cells[i - 1]
                cell = cells[i]
                right = cells[(i + 1) % len(cells)]
                next_gen += apply_rule30(cell, left, right)
        return next_gen

key_logs = []
# Generate the keys for encryption/decryption using Rule 30
def generate_keys(initial_key, iterations):
        keys = []
        decimal_keys = []
        formatted_keys = []
        current_gen = initial_key
        seen_keys = set()  # Set to store unique keys
        num = '01'
        global key_logs

        start_time = time.time()
        for _ in range(iterations):
                next_gen = generate_next_generation(current_gen)

                # Check for repetition
                while next_gen in seen_keys:
                        # print("Repetition detected. Adjusting next generation.")
                        next_gen = bin(int(next_gen, 2) + int(num, 2))[2:]
                        # print(next_gen)
                keys.append(next_gen)
                seen_keys.add(next_gen)

                # Convert binary key to decimal
                decimal_key = int(next_gen, 2)
                decimal_keys.append(decimal_key)

                current_gen = next_gen
        end_time = time.time()
        key_generation_time = end_time - start_time
        print(f"Time taken to generate keys: {key_generation_time:.6f} seconds \n")
        # Format keys for display
        formatted_keys.append(f"Time taken to generate keys: {key_generation_time:.6f} seconds\n")
        for i, key in enumerate(keys):
                formatted_key = f"{key} = {decimal_keys[i]}"
                formatted_keys.append(formatted_key)
        key_logs = formatted_keys
        # self.logTxt.setText('\n'.join(formatted_keys))
        return keys

process_logs = []
# Process the entire text using the provided initial key and iterations
def process_text(text, initial_key, iterations):
        keys = generate_keys(initial_key, iterations)
        processed_text = ""
        logText = []
        global process_logs

        start_time = time.time()
        for char in text:
                binary_character = format(ord(char), '08b')  # Convert character to binary
                process_binary = binary_character
                # self.processTxt.append("Character to process: "+char)
                logText.append(f"Character to process: {char}")
                
                # Perform XOR operation on each binary with all keys
                for index, key in enumerate(keys):
                        num1 = int(process_binary, 2)
                        num2 = int(key, 2)
                        temp = process_binary
                        process_binary = format(num1 ^ num2, '08b')
                        # self.processTxt.append(temp + " ⊕ " + key + "    = " + process_binary + "      = " + chr(int(process_binary, 2)))
                        logText.append(temp + " ⊕ " + key + "    = " + process_binary + "      = " + chr(int(process_binary, 2)))

                # self.processTxt.append("Character : "+char+"    Encrypted to : "+ chr(int(process_binary, 2))+"\n")
                logText.append(f"Character : {char}    Encrypted to : {chr(int(process_binary, 2))}\n")
                # Convert binary back to character and append it to the encrypted text
                processed_text += chr(int(process_binary, 2))

        end_time = time.time()
        encryption_time = end_time - start_time
        time_log = f"Time taken to Encrypt/Decrypt: {encryption_time:.6f} seconds\n"

        logText.insert(0, time_log)
        # logText.append(time_log)

        # Join logText entries into a single string with newlines
        process_logs = logText
        # self.processTxt.setText("\n".join(logText))
        print(f"Time taken to Encrypt/Decrypt: {encryption_time:.6f} seconds")
        return processed_text

# -----------------------------------------------------------------------------

def is_binary(text):
        for char in text:
                if char not in ('0', '1'):
                        return False
        return True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
