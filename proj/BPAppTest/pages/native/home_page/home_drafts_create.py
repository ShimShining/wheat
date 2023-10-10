#草稿箱
from base.UPath import UPath
from base.BP_app import BPApp
from pages.native.home_page.home_page import HomePage


class DraftsPage():

    #关闭新手引导
    def goto_drafts_home(self):
        self.find_and_click(self.__drafts_home)
        return self.enter_banner_map_detail()
