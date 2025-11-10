from classes.mainClass import PhysicsCalculator
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsCalculator()
    window.show()
    sys.exit(app.exec())
