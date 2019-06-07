# 分页
class Pagination(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=8, maxPageNum=5):
        '''

        :param totalCount: 所有数据的个数
        :param currentPage: 当前页
        :param perPageItemNum: 每页显示个数
        :param maxPageNum: 最多页面个数

        '''
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page - 1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        '''
        总页数
        :return:
        '''
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        # 当前页
        # self.current_page
        # 最多显示的页码数量
        # self.per_pager_num
        # 总页数
        # self.per_page_num
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages + 1)
        # 总页数特别多
        part = self.max_page_num // 2
        if self.current_page <= part:
            return range(1, self.max_page_num + 1)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/backend/index_seat?p=1'>首页</a></li>"
        page_list.append(first)

        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/backend/index_seat?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/backend/index_seat?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/backend/index_seat?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            next = "<li><a href='#'>下一页</a></li>"
        else:
            next = "<li><a href='/backend/index_seat?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(next)

        end = "<li><a href='/backend/index_seat?p=%s'>尾页</a></li>" % (self.num_pages)
        page_list.append(end)

        return ''.join(page_list)


class PaginationMovie(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=6, maxPageNum=2):
        '''
        :param totalCount: 所有数据的个数
        :param currentPage: 当前页
        :param perPageItemNum: 每页显示个数
        :param maxPageNum: 最多页面个数

        '''
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page - 1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        '''
        总页数
        :return:
        '''
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        # 当前页
        # self.current_page
        # 最多显示的页码数量
        # self.per_pager_num
        # 总页数
        # self.per_page_num
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages + 1)
        # 总页数特别多
        part = self.max_page_num // 2
        if self.current_page <= part:
            return range(1, self.max_page_num + 1)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/backend/index_movie/?p=1'>首页</a></li>"
        page_list.append(first)

        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/backend/index_movie/?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/backend/index_movie/?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/backend/index_movie/?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            next = "<li><a href='#'>下一页</a></li>"
        else:
            next = "<li><a href='/backend/index_movie/?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(next)

        end = "<li><a href='/backend/index_movie/?p=%s'>尾页</a></li>" % (self.num_pages)
        page_list.append(end)

        return ''.join(page_list)


class PaginationPlan(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=6, maxPageNum=2):
        '''
        :param totalCount: 所有数据的个数
        :param currentPage: 当前页
        :param perPageItemNum: 每页显示个数
        :param maxPageNum: 最多页面个数

        '''
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page - 1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        '''
        总页数
        :return:
        '''
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        # 当前页
        # self.current_page
        # 最多显示的页码数量
        # self.per_pager_num
        # 总页数
        # self.per_page_num
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages + 1)
        # 总页数特别多
        part = self.max_page_num // 2
        if self.current_page <= part:
            return range(1, self.max_page_num + 1)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/backend/index_plan/?p=1'>首页</a></li>"
        page_list.append(first)

        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/backend/index_plan/?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/backend/index_plan/?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/backend/index_plan/?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            next = "<li><a href='#'>下一页</a></li>"
        else:
            next = "<li><a href='/backend/index_plan/?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(next)

        end = "<li><a href='/backend/index_plan/?p=%s'>尾页</a></li>" % (self.num_pages)
        page_list.append(end)

        return ''.join(page_list)


class PaginationTicket(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=6, maxPageNum=2):
        '''
        :param totalCount: 所有数据的个数
        :param currentPage: 当前页
        :param perPageItemNum: 每页显示个数
        :param maxPageNum: 最多页面个数

        '''
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum

    def start(self):
        return (self.current_page - 1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        '''
        总页数
        :return:
        '''
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        # 当前页
        # self.current_page
        # 最多显示的页码数量
        # self.per_pager_num
        # 总页数
        # self.per_page_num
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages + 1)
        # 总页数特别多
        part = self.max_page_num // 2
        if self.current_page <= part:
            return range(1, self.max_page_num + 1)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        page_list = []
        first = "<li><a href='/backend/index_ticket/?p=1'>首页</a></li>"
        page_list.append(first)

        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/backend/index_ticket/?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/backend/index_ticket/?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/backend/index_ticket/?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            next = "<li><a href='#'>下一页</a></li>"
        else:
            next = "<li><a href='/backend/index_ticket/?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(next)

        end = "<li><a href='/backend/index_ticket/?p=%s'>尾页</a></li>" % (self.num_pages)
        page_list.append(end)

        return ''.join(page_list)