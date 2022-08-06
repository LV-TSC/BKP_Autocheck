select * from TBL_RECORDS where bkp_date = '2022/06/17'
select getdate()
update TBL_RECORDS set idstatus = 3

sp_helptext sp_create_daily_record
create procedure sp_create_daily_record as 
BEGIN
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (2, 2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (6, 2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (7, 2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (10,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (11,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (12,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (14,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (15,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (16,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (18,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (19,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (21,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (24,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (25,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (26,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (27,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (28,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (29,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (30,2, getdate() , 'SQL', getdate(), 1)
insert into TBL_RECORDS (idserver,idstatus,bkp_date,reg_user,reg_date,active) values (31,2, getdate() , 'SQL', getdate(), 1)
END




