create table team_info(tid int primary key,teamname char(20) unique);

create table user_info(uid int primary key,username char(20) unique,password char(20) not NULL,tid int,foreign key(tid) references team_info(tid));


create table challenge_topics(topic_id int primary key,cname char(20));

create table challenge(cid int primary key,topic_id int,value int,foreign key(topic_id) references challenge_topics(topic_id));

create table solve(topic_id int,uid int,score int,foreign key(topic_id) references challenge_topics(topic_id),foreign key(uid) references user_info(uid));

create table teamscore(topic_id int,tid int,solvescore int,primary key(topic_id,tid));

drop table test;
create table test(uid int primary key,username char(20),password char(20));