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

create table challenge(cid int,topic_id int,value int,flag char(40),primary key(cid,topic_id),foreign key(topic_id) references challenge_topics(topic_id));

create table solve(topic_id int,uid int,score int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));

create table teamscore(topic_id int,tid int,solvescore int,primary key(topic_id,tid),foreign key(tid) references team_info(tid));

-- //写触发器
-- 个人score更新
-- update solve set score = score+500 where uid=1;
-- update solve set score = score+(select value from challenge where topic_id='100' and cid=1) where uid=1;

-- //队伍成绩统计
-- update teamscore set solvescore=(select sum(score) from (select score from solve where uid in (select uid from user_info where tid=1))as a) werehere tid=1;

create table test(uid int primary key,username char(20),password char(20));
