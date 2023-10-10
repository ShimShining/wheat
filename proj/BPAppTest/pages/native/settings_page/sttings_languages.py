# -*- coding: utf-8 -*-
#此模块用于切换语言元素定位
from base.UPath import UPath
from base.BP_app import BPApp


class Langunges(BPApp):

    __language_English = {'android': UPath(text="English"), 'ios':""}#英语
    __language_Filipino = {'android': UPath(text="Filipino"), 'ios': ""}#菲律宾
    __language_German = {'android': UPath(text="Deutsch"), 'ios': ""}#德语
    __language_Indonesian = {'android': UPath(text="Bahasa Indonesia"), 'ios': ""}#印度尼西亚
    __language_Italian = {'android': UPath(text="Italiano"), 'ios': ""}#意大利
    __language_Japanese = {'android': UPath(text="日本語"), 'ios': ""}#日语
    __language_Korean = {'android': UPath(text="한국어"), 'ios': ""}#韩语
    __language_Malay  = {'android': UPath(text="Bahasa Melayu "), 'ios': ""}#马来西亚
    __language_Portuguese = {'android': UPath(text="Português"), 'ios': ""}#葡萄牙
    __language_Russian = {'android': UPath(text="русский"), 'ios': ""}#俄语
    __language_Spanish = {'android': UPath(text="Español"), 'ios': ""}#西班牙语
    __language_Thai = {'android': UPath(text="ภาษาไทย"), 'ios': ""}#泰国
    __language_Turkish = {'android': UPath(text="Türkçe"), 'ios': ""}#土耳其
    __language_Vietnamese = {'android': UPath(text="Tiếng Việt"), 'ios': ""}#越南语
    __Dend = {'android': UPath(host=True, resourceId="id/customBtnWithLoadingRoot"), 'ios': ""}#确认按钮
    a = [__language_English,__language_Filipino,__language_German,__language_Indonesian,__language_Japanese,__language_Korean,__language_Malay,__language_Portuguese,__language_Russian,__language_Spanish,__language_Thai,__language_Turkish,__language_Vietnamese]

    def sttings_languages_go(self):
        b=self.find_and_click(self.a)
        self.find_and_click(self.__language_Filipino)
        print(22)
        for a in b:
            a + 1
            print(11)


        self.find_and_click(self.__Dend)

        return