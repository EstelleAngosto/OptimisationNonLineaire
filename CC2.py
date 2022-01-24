# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CC2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

def exec_function(y,x):
        fct = ''
        for i in y :
            if i == 'x':
                fct+=str(x)
            else:
                fct+=i
        return eval(fct)

class Ui_Algorithme_recherche_window(object):
    def setupUi(self, Algorithme_recherche_window):
        Algorithme_recherche_window.setObjectName("Algorithme_recherche_window")
        Algorithme_recherche_window.resize(542, 232)
        self.centralwidget = QtWidgets.QWidget(Algorithme_recherche_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.tabWidget.setObjectName("tabWidget")
        self.recherche_pas_tab = QtWidgets.QWidget()
        self.recherche_pas_tab.setObjectName("recherche_pas_tab")
        self.valider_pas_butt = QtWidgets.QPushButton(self.recherche_pas_tab)
        self.valider_pas_butt.setGeometry(QtCore.QRect(260, 120, 93, 28))
        self.valider_pas_butt.setObjectName("valider_pas_butt")
        self.reset_pas_butt = QtWidgets.QPushButton(self.recherche_pas_tab)
        self.reset_pas_butt.setGeometry(QtCore.QRect(360, 120, 93, 28))
        self.reset_pas_butt.setObjectName("reset_pas_butt")
        self.fonction_pas_led = QtWidgets.QLineEdit(self.recherche_pas_tab)
        self.fonction_pas_led.setGeometry(QtCore.QRect(120, 50, 331, 22))
        self.fonction_pas_led.setObjectName("fonction_pas_led")
        self.q1_pas_butt = QtWidgets.QPushButton(self.recherche_pas_tab)
        self.q1_pas_butt.setGeometry(QtCore.QRect(160, 120, 93, 28))
        self.q1_pas_butt.setObjectName("q1_pas_butt")
        self.pas_fixe_rdb = QtWidgets.QRadioButton(self.recherche_pas_tab)
        self.pas_fixe_rdb.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.pas_fixe_rdb.setObjectName("pas_fixe_rdb")
        self.pas_accelere_rdb = QtWidgets.QRadioButton(self.recherche_pas_tab)
        self.pas_accelere_rdb.setGeometry(QtCore.QRect(120, 20, 95, 20))
        self.pas_accelere_rdb.setObjectName("pas_accelere_rdb")
        self.fonction_pas_lbl = QtWidgets.QLabel(self.recherche_pas_tab)
        self.fonction_pas_lbl.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.fonction_pas_lbl.setObjectName("fonction_pas_lbl")
        self.valdep_pas_lbl = QtWidgets.QLabel(self.recherche_pas_tab)
        self.valdep_pas_lbl.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.valdep_pas_lbl.setObjectName("valdep_pas_lbl")
        self.valdep_pas_dsb = QtWidgets.QDoubleSpinBox(self.recherche_pas_tab)
        self.valdep_pas_dsb.setGeometry(QtCore.QRect(120, 80, 62, 22))
        self.valdep_pas_dsb.setMinimum(-1000.0)
        self.valdep_pas_dsb.setMaximum(1000.0)
        self.valdep_pas_dsb.setObjectName("valdep_pas_dsb")
        self.valpas_pas_lbl = QtWidgets.QLabel(self.recherche_pas_tab)
        self.valpas_pas_lbl.setGeometry(QtCore.QRect(210, 80, 91, 16))
        self.valpas_pas_lbl.setObjectName("valpas_pas_lbl")
        self.valpas_pas_dsb = QtWidgets.QDoubleSpinBox(self.recherche_pas_tab)
        self.valpas_pas_dsb.setGeometry(QtCore.QRect(300, 80, 91, 22))
        self.valpas_pas_dsb.setDecimals(7)
        self.valpas_pas_dsb.setMinimum(-1000.0)
        self.valpas_pas_dsb.setMaximum(1000.0)
        self.valpas_pas_dsb.setObjectName("valpas_pas_dsb")
        self.tabWidget.addTab(self.recherche_pas_tab, "")
        self.bissection_tab = QtWidgets.QWidget()
        self.bissection_tab.setObjectName("bissection_tab")
        self.reset_bis_butt = QtWidgets.QPushButton(self.bissection_tab)
        self.reset_bis_butt.setGeometry(QtCore.QRect(330, 90, 93, 28))
        self.reset_bis_butt.setObjectName("reset_bis_butt")
        self.valider_bis_butt = QtWidgets.QPushButton(self.bissection_tab)
        self.valider_bis_butt.setGeometry(QtCore.QRect(230, 90, 93, 28))
        self.valider_bis_butt.setObjectName("valider_bis_butt")
        self.q1_bis_butt = QtWidgets.QPushButton(self.bissection_tab)
        self.q1_bis_butt.setGeometry(QtCore.QRect(130, 90, 93, 28))
        self.q1_bis_butt.setObjectName("q1_bis_butt")
        self.fonction_bis_lbl = QtWidgets.QLabel(self.bissection_tab)
        self.fonction_bis_lbl.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.fonction_bis_lbl.setObjectName("fonction_bis_lbl")
        self.fonction_bis_led = QtWidgets.QLineEdit(self.bissection_tab)
        self.fonction_bis_led.setGeometry(QtCore.QRect(90, 10, 331, 22))
        self.fonction_bis_led.setObjectName("fonction_bis_led")
        self.valmax_bis_dsb = QtWidgets.QDoubleSpinBox(self.bissection_tab)
        self.valmax_bis_dsb.setGeometry(QtCore.QRect(260, 40, 62, 22))
        self.valmax_bis_dsb.setMaximum(1000.0)
        self.valmax_bis_dsb.setObjectName("valmax_bis_dsb")
        self.valmin_bis_lbl = QtWidgets.QLabel(self.bissection_tab)
        self.valmin_bis_lbl.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.valmin_bis_lbl.setObjectName("valmin_bis_lbl")
        self.valmax_bis_lbl = QtWidgets.QLabel(self.bissection_tab)
        self.valmax_bis_lbl.setGeometry(QtCore.QRect(180, 40, 91, 16))
        self.valmax_bis_lbl.setObjectName("valmax_bis_lbl")
        self.valmin_bis_dsb = QtWidgets.QDoubleSpinBox(self.bissection_tab)
        self.valmin_bis_dsb.setGeometry(QtCore.QRect(90, 40, 62, 22))
        self.valmin_bis_dsb.setDecimals(2)
        self.valmin_bis_dsb.setMinimum(-1000.0)
        self.valmin_bis_dsb.setMaximum(1000.0)
        self.valmin_bis_dsb.setObjectName("valmin_bis_dsb")
        self.epsilon_bis_dsb = QtWidgets.QDoubleSpinBox(self.bissection_tab)
        self.epsilon_bis_dsb.setGeometry(QtCore.QRect(400, 40, 91, 22))
        self.epsilon_bis_dsb.setDecimals(7)
        self.epsilon_bis_dsb.setMaximum(100.0)
        self.epsilon_bis_dsb.setObjectName("epsilon_bis_dsb")
        self.epsilon_bis_lbl = QtWidgets.QLabel(self.bissection_tab)
        self.epsilon_bis_lbl.setGeometry(QtCore.QRect(350, 40, 91, 16))
        self.epsilon_bis_lbl.setObjectName("epsilon_bis_lbl")
        self.tabWidget.addTab(self.bissection_tab, "")
        self.Newton_tab = QtWidgets.QWidget()
        self.Newton_tab.setObjectName("Newton_tab")
        self.reset_newton_butt = QtWidgets.QPushButton(self.Newton_tab)
        self.reset_newton_butt.setGeometry(QtCore.QRect(360, 140, 93, 28))
        self.reset_newton_butt.setObjectName("reset_newton_butt")
        self.valider_newton_butt = QtWidgets.QPushButton(self.Newton_tab)
        self.valider_newton_butt.setGeometry(QtCore.QRect(260, 140, 93, 28))
        self.valider_newton_butt.setObjectName("valider_newton_butt")
        self.q2_newton_butt = QtWidgets.QPushButton(self.Newton_tab)
        self.q2_newton_butt.setGeometry(QtCore.QRect(160, 140, 93, 28))
        self.q2_newton_butt.setObjectName("q2_newton_butt")
        self.fonction_newton_lbl = QtWidgets.QLabel(self.Newton_tab)
        self.fonction_newton_lbl.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.fonction_newton_lbl.setObjectName("fonction_newton_lbl")
        self.fonction_newton_led = QtWidgets.QLineEdit(self.Newton_tab)
        self.fonction_newton_led.setGeometry(QtCore.QRect(120, 10, 331, 22))
        self.fonction_newton_led.setObjectName("fonction_newton_led")
        self.derive_newton_lbl = QtWidgets.QLabel(self.Newton_tab)
        self.derive_newton_lbl.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.derive_newton_lbl.setObjectName("derive_newton_lbl")
        self.derive_newton_led = QtWidgets.QLineEdit(self.Newton_tab)
        self.derive_newton_led.setGeometry(QtCore.QRect(120, 40, 331, 22))
        self.derive_newton_led.setObjectName("derive_newton_led")
        self.derivesec_newton_lbl = QtWidgets.QLabel(self.Newton_tab)
        self.derivesec_newton_lbl.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.derivesec_newton_lbl.setObjectName("derivesec_newton_lbl")
        self.derivesec_newton_led = QtWidgets.QLineEdit(self.Newton_tab)
        self.derivesec_newton_led.setGeometry(QtCore.QRect(120, 70, 331, 22))
        self.derivesec_newton_led.setObjectName("derivesec_newton_led")
        self.epsilon_newton_dsb = QtWidgets.QDoubleSpinBox(self.Newton_tab)
        self.epsilon_newton_dsb.setGeometry(QtCore.QRect(270, 100, 91, 22))
        self.epsilon_newton_dsb.setDecimals(7)
        self.epsilon_newton_dsb.setMaximum(100.0)
        self.epsilon_newton_dsb.setObjectName("epsilon_newton_dsb")
        self.valdep_newton_lbl = QtWidgets.QLabel(self.Newton_tab)
        self.valdep_newton_lbl.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.valdep_newton_lbl.setObjectName("valdep_newton_lbl")
        self.epsilon_newton_lbl = QtWidgets.QLabel(self.Newton_tab)
        self.epsilon_newton_lbl.setGeometry(QtCore.QRect(210, 100, 51, 16))
        self.epsilon_newton_lbl.setObjectName("epsilon_newton_lbl")
        self.valdep_newton_dsb = QtWidgets.QDoubleSpinBox(self.Newton_tab)
        self.valdep_newton_dsb.setGeometry(QtCore.QRect(120, 100, 62, 22))
        self.valdep_newton_dsb.setMinimum(-1000.0)
        self.valdep_newton_dsb.setMaximum(1000.0)
        self.valdep_newton_dsb.setObjectName("valdep_newton_dsb")
        self.tabWidget.addTab(self.Newton_tab, "")
        Algorithme_recherche_window.setCentralWidget(self.centralwidget)
        
        self.q1_pas_butt.clicked.connect(self.set_q1_pas)
        self.q1_bis_butt.clicked.connect(self.set_q1_bis)
        self.q2_newton_butt.clicked.connect(self.set_q2)
        self.valider_pas_butt.clicked.connect(self.recherche_pas)
        self.valider_bis_butt.clicked.connect(self.bissection)
        self.valider_newton_butt.clicked.connect(self.newton)
        self.reset_pas_butt.clicked.connect(lambda: self.reset(self.reset_pas_butt))
        self.reset_bis_butt.clicked.connect(lambda: self.reset(self.reset_bis_butt))
        self.reset_newton_butt.clicked.connect(lambda: self.reset(self.reset_newton_butt))

        self.retranslateUi(Algorithme_recherche_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Algorithme_recherche_window)

    def retranslateUi(self, Algorithme_recherche_window):
        _translate = QtCore.QCoreApplication.translate
        Algorithme_recherche_window.setWindowTitle(_translate("Algorithme_recherche_window", "MainWindow"))
        self.valider_pas_butt.setText(_translate("Algorithme_recherche_window", "Valider"))
        self.reset_pas_butt.setText(_translate("Algorithme_recherche_window", "Reset"))
        self.q1_pas_butt.setText(_translate("Algorithme_recherche_window", "Question 1"))
        self.pas_fixe_rdb.setText(_translate("Algorithme_recherche_window", "Pas fixe"))
        self.pas_accelere_rdb.setText(_translate("Algorithme_recherche_window", "Pas accéléré"))
        self.fonction_pas_lbl.setText(_translate("Algorithme_recherche_window", "Fonction"))
        self.valdep_pas_lbl.setText(_translate("Algorithme_recherche_window", "Point de départ"))
        self.valpas_pas_lbl.setText(_translate("Algorithme_recherche_window", "Valeur du pas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recherche_pas_tab), _translate("Algorithme_recherche_window", "Recherche par pas"))
        self.reset_bis_butt.setText(_translate("Algorithme_recherche_window", "Reset"))
        self.valider_bis_butt.setText(_translate("Algorithme_recherche_window", "Valider"))
        self.q1_bis_butt.setText(_translate("Algorithme_recherche_window", "Question 1"))
        self.fonction_bis_lbl.setText(_translate("Algorithme_recherche_window", "Fonction"))
        self.valmin_bis_lbl.setText(_translate("Algorithme_recherche_window", "Valeur min."))
        self.valmax_bis_lbl.setText(_translate("Algorithme_recherche_window", "Valeur max."))
        self.epsilon_bis_lbl.setText(_translate("Algorithme_recherche_window", "Epsilon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bissection_tab), _translate("Algorithme_recherche_window", "Recherche par bissection"))
        self.reset_newton_butt.setText(_translate("Algorithme_recherche_window", "Reset"))
        self.valider_newton_butt.setText(_translate("Algorithme_recherche_window", "Valider"))
        self.q2_newton_butt.setText(_translate("Algorithme_recherche_window", "Question 2"))
        self.fonction_newton_lbl.setText(_translate("Algorithme_recherche_window", "Fonction"))
        self.derive_newton_lbl.setText(_translate("Algorithme_recherche_window", "Dérivé"))
        self.derivesec_newton_lbl.setText(_translate("Algorithme_recherche_window", "Dérivée seconde"))
        self.valdep_newton_lbl.setText(_translate("Algorithme_recherche_window", "Point de départ"))
        self.epsilon_newton_lbl.setText(_translate("Algorithme_recherche_window", "Epsilon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Newton_tab), _translate("Algorithme_recherche_window", "Newton-Raphson"))

    def set_q1_pas(self):
        self.pas_fixe_rdb.setChecked(True)
        self.fonction_pas_led.setText("x**5-5*x**3-20*x+5")
        self.valdep_pas_dsb.setValue(0)
        self.valpas_pas_dsb.setValue(0.05)
        
    def set_q1_bis(self):
        self.fonction_bis_led.setText("x**5-5*x**3-20*x+5")
        self.valmax_bis_dsb.setValue(5)
        self.valmin_bis_dsb.setValue(-5)
        self.epsilon_bis_dsb.setValue(0.1)
        
    def set_q2(self):
        self.fonction_newton_led.setText("x**3-7*x**2+8*x-3")
        self.derive_newton_led.setText("3*x**2-14*x+8")
        self.derivesec_newton_led.setText("6*x-14")
        self.valdep_newton_dsb.setValue(5)
        self.epsilon_newton_dsb.setValue(0.0001)
    
    def reset(self, b):
            
        name = b.objectName()
                
        if name == "reset_pas_butt":
            self.fonction_pas_led.setText("")
            self.valdep_pas_dsb.setValue(0)
            self.valpas_pas_dsb.setValue(0)

        if name == "reset_bis_butt":
            self.fonction_bis_led.setText("")
            self.valmin_bis_dsb.setValue(0)
            self.valmax_bis_dsb.setValue(0)
            self.epsilon_bis_dsb.setValue(0)

        if name == "reset_newton_butt":
            self.fonction_newton_led.setText("")
            self.derive_newton_led.setText("")
            self.derivesec_newton_led.setText("")
            self.valdep_newton_dsb.setValue(0)
            self.epsilon_newton_dsb.setValue(0)
    
    def recherche_pas(self):
        
        print("Recherche par pas : ")
        
        function = self.fonction_pas_led.text()
        x1 = self.valdep_pas_dsb.value()
        pas = self.valpas_pas_dsb.value()
        fixe = self.pas_fixe_rdb.isChecked()
                
        f1 = exec_function(function,x1)
        x2 = x1-pas
        f2 = exec_function(function,x2)
        i = 0
        
        if f2 > f1 :
            x2 = x1+pas
            f2 = exec_function(function,x2)
            while f1>=f2 : 
                i = i+1
                x1 = x2
                if fixe == False :
                    pas = pas*2
                x2 = x1+pas
                f1 = exec_function(function,x1)
                f2 = exec_function(function,x2)
                print("Etape "+str(i))
                print (str(x1)+" "+str(f1)+" "+str(x2)+" "+str(f2))
            print("La solution est entre "+str(x1)+" et "+str(x2)+".")

        elif f2 < f1 :
            while f1>=f2 : 
                i = i+1
                x1 = x2
                if fixe == False:
                    pas = pas*2
                x2 = x1-pas
                f1 = exec_function(function,x1)
                f2 = exec_function(function,x2)
                print("Etape "+str(i))
                print (str(x1)+" "+str(f1)+" "+str(x2)+" "+str(f2))
            print("La solution est entre "+str(x1)+" et "+str(x2)+".")
    
        elif f2 == f1 : 
            print("La solution est entre "+str(x1)+" et "+str(x2)+".") 
        
    def bissection(self):
        
        print("Recherche par bissection : ")
        
        function = self.fonction_bis_led.text()
        interval_min = self.valmin_bis_dsb.value()
        interval_max = self.valmax_bis_dsb.value()
        epsilon = self.epsilon_bis_dsb.value()
        
        L0 = interval_max-interval_min
        i = 0
        
        while L0>epsilon:
           
            quart = (interval_max-interval_min)/4
        
            point_milieu = interval_min+2*quart
            point_quart1 = interval_min+quart
            point_quart2 = interval_min+3*quart
        
            print("Point milieu : "+str(point_milieu))
            print("Point quart 1 : "+str(point_quart1))
            print("Point quart 2 : "+str(point_quart2))
        
            fPoint_milieu = exec_function(function, point_milieu)
            fPoint_quart1 = exec_function(function, point_quart1)
            fPoint_quart2 = exec_function(function, point_quart2)
        
            print("f(Point milieu) : "+str(fPoint_milieu))
            print("f(Point quart 1) : "+str(fPoint_quart1))
            print("f(Point quart 2) : "+str(fPoint_quart2))
        
            if fPoint_quart2 > fPoint_milieu > fPoint_quart1:
                interval_max = point_milieu
            
        
            if fPoint_quart2 < fPoint_milieu < fPoint_quart1:
                interval_min = point_milieu
        
            if fPoint_quart2 > fPoint_milieu and fPoint_quart1 > fPoint_milieu:
                interval_min = point_quart1
                interval_max = point_quart2
            
            i+=1
            print("Etape : "+str(i))
            print("Nouvelle intervalle : "+str([interval_min,interval_max]))
            L0 = interval_max-interval_min
            print("Nouvelle valeur de L0 :"+str(L0))
        
        print("Valeur optimale : "+str(point_milieu)+", Résultat de la fonction : ",str(fPoint_milieu))
            
    def newton(self):
        
        print("Recherche par Newton-Raphson : ")
       
        x = self.valdep_newton_dsb.value()
        epsilon = self.epsilon_newton_dsb.value()
        devfonc = self.derive_newton_led.text()
        secdevfonc = self.derivesec_newton_led.text()
        valderive = exec_function(devfonc, x)
        valsecderive = exec_function(secdevfonc, x)
        i = 0
        
        while abs(valderive)>epsilon:
            print ("Etape "+str(i))
            print ("x : "+str(x))
            print("Dérivé de x : "+str(valderive))
            print("Dérivé seconde de x : "+str(valsecderive))
            x = x - valderive/valsecderive
            valderive = exec_function(devfonc,x)
            valsecderive = exec_function(secdevfonc,x)
            i = i+1
    
        print("Résultat final : "+str(x))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Algorithme_recherche_window = QtWidgets.QMainWindow()
    ui = Ui_Algorithme_recherche_window()
    ui.setupUi(Algorithme_recherche_window)
    Algorithme_recherche_window.show()
    sys.exit(app.quit())

