# 1. 提交记录
## 1.1. 新增题解
【新增题解】【002计算某字符出现次数】
【新增题解】【HJ3明明的随机数】题解1：使用count方法
## 1.2. 更新题解
【更新题解】【002计算某字符出现次数】
## 1.3. 新增快捷访问方式
【新增快捷访问方式】HJ1字符串最后一个单词的长度
## 1.4. 更新快捷访问方式
【更新快捷访问方式】HJ4字符串分隔
## 1.2. 更新文件
【更新ReadMe.md】
【更新.gitignore】
【更新debugProj/main.py】

# 2. 牛客华为机试题库题解博客

题库链接: https://www.nowcoder.com/ta/huawei

023删除字符串中出现次数最少的字符: https://blog.csdn.net/COCO56/article/details/124653103
022汽水瓶: https://blog.csdn.net/COCO56/article/details/124643017
021简单密码: https://blog.csdn.net/COCO56/article/details/124640587
020密码验证合格程序: https://blog.csdn.net/COCO56/article/details/124617142
019简单错误记录: https://blog.csdn.net/COCO56/article/details/124599372
018识别有效的IP地址和掩码并进行分类统计: https://blog.csdn.net/COCO56/article/details/124596071
017坐标移动: https://blog.csdn.net/COCO56/article/details/124579232
016购物单: https://blog.csdn.net/COCO56/article/details/124463397
015求int型正整数在内存中存储时1的个数: https://blog.csdn.net/COCO56/article/details/124370584
014字符串排序: https://blog.csdn.net/COCO56/article/details/124369826
013句子逆序: https://blog.csdn.net/COCO56/article/details/124369555
012字符串反转: https://blog.csdn.net/COCO56/article/details/124369087
011数字颠倒: https://blog.csdn.net/COCO56/article/details/124368903
010字符个数统计: https://blog.csdn.net/COCO56/article/details/124368525
009提取不重复的整数: https://blog.csdn.net/COCO56/article/details/124368327
008合并表记录: https://blog.csdn.net/COCO56/article/details/124367871
007取近似值: https://blog.csdn.net/COCO56/article/details/124366811
006质数因子: https://blog.csdn.net/COCO56/article/details/124362090
005进制转换: https://blog.csdn.net/COCO56/article/details/124359925
004字符串分隔: https://blog.csdn.net/COCO56/article/details/124357977
003明明的随机数: https://coco56.blog.csdn.net/article/details/124357365
002计算某字符出现次数: https://blog.csdn.net/COCO56/article/details/124356704
001字符串最后一个单词的长度: https://blog.csdn.net/COCO56/article/details/124355536

# 3. 注意事项

牛客华为机试题库——https://www.nowcoder.com/ta/huawei（重点看）
牛客在线编程算法篇——https://www.nowcoder.com/exam/oj

第一轮是笔试，一共三道题，总共400分，分别是100分，100分，200分，难度为leetcode简单到中等难度，考试过150分即合格。考试平台为牛客网，可以先上到网站华为编程专区练习熟悉考试环境。
注意：可以本地ide或者eclipse，但是不要访问其他网页或本地资料。
练习时，一般只需要写一个function，输入输出已经固定，但是考试，有可能答题区是一片空白，此时注意要写的是main函数，从控制台读取输入输出，比如java可能就会用到Scanner(System.in)之类的，python会用到readline之类的，这个到时候别一下子懵了哈。可以网上看看这类练习。
练习地址: https://www.nowcoder.com/ta/huawei

您先练习熟悉一下，后期会发个笔试链接，笔试链接有效期很长，可以准备好了以后有空的时候考下。笔试链接打开之后考试就开始了，结束之前一定要提交答案。注意：考试分数越高越好
一、       总览
总共3到编程题，考试时长150分钟，共400分，150分算通过，第1/2道题属于基础题，分数为100，第3道题稍微复杂，分数为200。做题攻略：前面两道尽量用时45分钟，第三道题用时60分钟，优先将前面两道做完整，第三道题一定要做，这样可以提高分数。考试过程中允许使用本地编译器，不受跳出次数限制，若有提示，请忽略；因不熟悉编译环境导致的考试不通过不予重测，请准备完毕后再点机试链接做题。
二、       判分标准
1、代码规范及可读性
最基本的要求，需要大家都能保证。不要随意命名、建议使用一种命名风格。禁止出现如下这种将代码写到一行的。完成代码后，将代码里面多余的注释、不用的代码等删掉再提交。
2、基本测试用例通过率
保证基本的用例能通过。算法实现后自测相关数据。
3、边缘测试用例通过率
算法实现后需要根据题目去自测边缘的相关数据。
三、       做题方法
牛客网的题目与leetcode等网站不一样，leetcode会给一个接口名，考生只需要实现该接口即可，而牛客网的题目不仅需要实现题目本身的算法内容，还需要接收输入和打印输出。
1、处理输入：将题目中描述的输入存入到变量中，大家可以提前熟悉下怎么获取输入。
2、接口实现：（建议：可以独立一个接口出来实现，将输入的数据传入这个接口处理，然后该接口返回输出数据。这种做法便于后续测试，测试时可以独立测试这个接口。）
3、处理输出：一般是将数据输出到控制台。
四、       必练题型
1、    输入输出样题
90%以上的人败在输入的处理上，机考题目本身并不复杂，请各位注意一定练习，否则遇到较难处理的输入时会导致题目不过。
OJ在线编程常见输入输出练习：https://www.nowcoder.com/test/27976983/summary#question
   必练输入题：https://ac.nowcoder.com/acm/contest/5657/J 此题必须练习，熟悉如何处理较为复杂的输入和输出。https://ac.nowcoder.com/acm/contest/5657#question 该链接可以查看正确答案。
2、    算法、知识点
数学知识：素数、公约数、矩阵等
重要数据结构知识：字符串（概率很大）、数组（概率很大）、链表、队列、堆、栈、map/set，以及它们的排序算法。树、图等可以自行准备，考的概率不大。
字符串最后一个单词的长度、二叉树的遍历、最大括号深度、春游名单、勾股数元组
华为在线笔试练习链接：https://www.nowcoder.com/ta/huawei
（开始考试时，务必关闭无关程序和网页等，打开摄像头，后台若检测有作弊嫌疑，可能机试不过）
争取准确率在80%，这样就比较安全


您好，机考指导如下：
（1）机考时间是150分钟，总分400分，三道编程题。机试难度不大，建议考到300分以上
（2）可以在牛客网进行编程练习，百度搜索牛客网-》题库-》在线编程-》算法篇-》面试高频榜单，大概要刷20～30道题目，一般就能通过机试。
100分试题
1. 连续字母长度
2. 判断连续字符串序列
3. 最长连续子序列
4. 最长子字符串长度
5. 英文输入法
6. 火星文计算
7. 字符串统计
8. 太阳能板最大面积
9. 工号不够用了怎么办
9. 英文输入法
10. 消消乐游戏
11. 敏感字段加密
12. 停车场车辆统计
13. we are a  team
14. 流水线
15. 最大花费金额
16. 猴子爬山
17. 最长的顺子
18. 按单词下标区间翻转文章内容
19. 用户调度问题
20. TLV解码
21. 矩形相交的面积
22. 构成正方形的数量
23. 最大矩阵和
24. 数组组成的最小数字
25. 数据分类
26. 两数之和的绝对值最小
27. 最大括号深度
28. 快递运输

200分试题：
1. 没有回文字符串
2. 字符串比较
3. 求满足条件的最长子串的长度
4. 文本统计分析
5. 欢乐的周末
6. 火锅
7. 跳格子游戏
8. 德州扑克
9. 可以组成网络的服务器
10. 计算疫情扩散时间
11. 解密犯罪时间
12. 数字排列
13. 出错的或电话
14. 考古学家
15. 目录删除
16. 转骰子
17. 采样过滤

总共有三道机试题，前两题每题100分，最后一道题200分。上面给出的100分题和200分题，但并不是全部题库，可以参考一下，感受一下难度。百度可以搜索华为机试+上面的试题，其中有一部分可以在牛客或者乐扣上在线编程。