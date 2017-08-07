import wx

import GUI
import re

Scale = [0, 5, 5]  # 计算音阶差
KeyMap = {"01": -11, "#01": -10, "02": -9, "#02": -8, "03": -7, "04": -6, "#04": -5, "05": -4, "#05": -3, "06": -2,
          "#06": -1, "07": 0,
          "1": 1, "#1": 2, "2": 3, "#2": 4, "3": 5, "4": 6, "#4": 7, "5": 8, "#5": 9, "6": 10, "#6": 11, "7": 12,
          "11": 13, "#11": 14, "22": 15, "#22": 16, "33": 17, "44": 18, "#44": 19, "55": 20, "#55": 21, "66": 22,
          "#66": 23, "77": 24}
NumKey = {y: x for x, y in KeyMap.items()}

InputText = ""
ChangeText = ""


class MainWindow(GUI.TuneChangeGui):
    def init_main_window(self):
        return

    def ClearAll(self, event):
        self.Before.Clear()
        self.After.Clear()

    def ChangeStart(self, event):
        global InputText
        InputText = self.Before.GetValue()
        self.TuneChange()

    def TuneChange(self):
        MidList = re.sub(",|，|\s", " ", InputText)
        MidList = re.split(",|，|\s", MidList)

        Scale[0] = Scale[1] - Scale[2]

        NumList = list(map(lambda x: KeyMap[x], MidList))
        ChangeList = list(map(lambda x: x + Scale[0], NumList))
        ChangeList = list(map(lambda x: NumKey[x], ChangeList))
        global ChangeText
        ChangeText = ",".join(ChangeList)
        self.After.SetValue(ChangeText)
        # if re.match(r'\[0-7]{1-2}.+?'):
        #     self.After.SetValue(InputText)
        #     print(InputText)
        # else:
        #     self.After.SetValue("输入格式错误")
        #     #print(InputText)

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
    mainWin.Center()
    mainWin.Show()
    app.MainLoop()
