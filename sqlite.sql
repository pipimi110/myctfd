drop table team_info;
drop table user_info;
drop table challenge_topics;
drop table challenge;
drop table solve;
drop table teamscore;
drop table test;

create table team_info(tid INTEGER primary key autoincrement,teamname char(20) unique not NULL,password char(20) not NULL,website char(20),affiliation char(20),country char(20));

create table user_info(uid INTEGER primary key autoincrement,username char(20) unique not NULL,password char(20) not NULL,tid int,foreign key(tid) references team_info(tid));

create table challenge_topics(topic_id int primary key,cname char(20));
insert into challenge_topics value(1,"xxxctf");

drop table challenge;
create table challenge(cid int DEFAULT 0,topic_id int DEFAULT 1,name char(20),category char(20),value int,desc char(40),flag char(40),solve_count int DEFAULT 0,primary key(cid,topic_id),foreign key(topic_id) references challenge_topics(topic_id));
-- 触发器 实现cid自增
CREATE TRIGGER addChallenge after insert on challenge begin update challenge set cid=(1+(select MAX(cid) from challenge)) where cid=new.cid;end;

insert into challenge(name,category,value,desc,flag) values("web1","Web",100,"do you know ff12","flag{f12_is_easy}");
insert into challenge(name,category,value,desc,flag) values("web2","Web",100,"do you know ff12","flag{f13_is_easy}");
insert into challenge(name,category,value,desc,flag) values("web3","Web",100,"do you know ff12","flag{f14_is_easy}");
insert into challenge(name,category,value,desc,flag) values("signIn","Misc",100,"flag{xxx}","flag{xxx}");
-- 标记用户做的题目
-- create table solve(topic_id int,uid int,score int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));
create table solve(topic_id int DEFAULT 1,uid int,cid int,primary key(uid,cid),foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid),foreign key(cid) references challenge(cid));
-- 触发器
create trigger addSolves after insert on solve begin update challenge set solve_count=solve_count+1 where cid=new.cid; end;


--- 标记队伍做的题目
-- create table teamsolve(topic_id int DEFAULT 1,tid int,cid int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(tid) references team_info(tid),foreign key(cid) references challenge(cid));

create table teamscore(topic_id int,tid int,solvescore int,primary key(topic_id,tid),foreign key(tid) references team_info(tid));

-- //写触发器
-- 个人score更新
-- update solve set score = score+500 where uid=1;
-- update solve set score = score+(select value from challenge where topic_id='100' and cid=1) where uid=1;

-- //队伍成绩统计
-- update teamscore set solvescore=(select sum(score) from (select score from solve where uid in (select uid from user_info where tid=1))as a) werehere tid=1;

create table test(uid int primary key,username char(20),password char(20));
