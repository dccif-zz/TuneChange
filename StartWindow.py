import wx
import GUI

Scale = [0, 5, 5]   #计算音阶差
TuneKey = {"1": "1",
           "2": "#1",
           "3": "2",
           "4": "#2",
           "5": "3",
           "6": "4",
           "7": "#4",
           "8": "5",
           "9": "#5",
           "10": "6",
           "11": "#6",
           "12": "7"}

class MainWindow(GUI.TuneChangeGui):

    def init_main_window(self):
        self.Before.SetValue("初始化测试")
        self.After.SetValue("测试")

    def ClearAll(self, event):
        self.Before.Clear()
        self.After.Clear()

    def ChangeStart(self, event):
        self.Before.SetValue("添加测试")
        Scale[0] = Scale[1] - Scale[2]
        print(Scale)

    def BeforeChoice(self, event):
        Scale[1] = self.Choice1.GetSelection()
        return

    def AfterChoice(self, event):
        Scale[2] = self.Choice2.GetSelection()
        return

if __name__ == "__main__":
    app = wx.App()
    mainWin = MainWindow(None)
    mainWin.init_main_window()
    mainWin.Show()
    app.MainLoop()
