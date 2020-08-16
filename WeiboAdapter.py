from chatterbot.logic import LogicAdapter
from urllib import request
import json

class WeiboLogicAdapter(LogicAdapter):



    def __init__(self, chatbot,**kwargs):
        super().__init__(chatbot,**kwargs)
        self.id='5915557360'
        self.proxy_addr='122.241.72.191:808'
        
    def can_process(self, statement):
       return statement.text.find("微博") >= 0        
        
        
    def use_proxy(self,url,proxy_addr):
        req=request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
        proxy=request.ProxyHandler({'http':proxy_addr})
        opener=request.build_opener(proxy,request.HTTPHandler)
        request.install_opener(opener)
        data=request.urlopen(req).read().decode('utf-8','ignore')
        return data
    
    def get_containerid(self,url):
        data=self.use_proxy(url,self.proxy_addr)
        content=json.loads(data).get('data')
        for data in content.get('tabsInfo').get('tabs'):
            if(data.get('tab_type')=='weibo'):
                containerid=data.get('containerid')
        return containerid
    def get_weibo(self,id):
        i=1
        contentlist=[]
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+self.get_containerid(url)+'&page='+str(i)
        try:
            data=self.use_proxy(weibo_url,self.proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(2):
                    card_type=cards[j].get('card_type')
                    if(card_type==9):
                        mblog=cards[j].get('mblog')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        created_at=mblog.get('created_at')
                        reposts_count=mblog.get('reposts_count')
                        scheme=cards[j].get('scheme')
                        text=mblog.get('text')
                        contentlist.append("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
            return contentlist
        except Exception as e:
            print(e)
            pass

    def process(self, input_statement,additional_response_selection_parameters=None):
        rst_statement=input_statement
        
        try:
            
            contentlist = self.get_weibo( self.id )
            print(contentlist[0])
            rst_statement.text = '\n'.join(contentlist)
        except Exception as e:
            print( e )
            rst_statement.text = "提取微博时出错了哦~"

        rst_statement.confidence = 1.0

        return rst_statement

