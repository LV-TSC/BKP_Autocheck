select ts.server_name,tst.state_name,tr.bkp_date from TBL_RECORDS TR 
inner join TBL_SERVER TS on TS.id = TR.idserver
inner join TBL_STATES TST on TST.id = TR.idstatus
where tr.bkp_date between GETDATE() -1 and GETDATE()


select * from TBL_RECORDS where idserver in('31') and bkp_date = '2022/06/17'
select * from TBL_RECORDS where bkp_date = '2022/06/18'
select * from TBL_RECORDS where bkp_date = convert(date,'2022/06/18')

update TBL_RECORDS set idstatus = '3' where idserver in('14','15') and bkp_date = '2022/06/16'

--CORRECTO
use SRV_BACKUP update TBL_RECORDS set idstatus = '2', reg_user = '', reg_date = '' where idserver = '2' and bkp_date = '2022-07-13'
--ERROR
update TBL_RECORDS set idstatus = '3' where idserver = '2' and bkp_date = '2022-07-13'


select * from TBL_STATES
select* from TBL_SERVER where bkp_active = '1'
select* from TBL_TYPE

select* from TBL_SERVER where id_type = '3'


update TBL_RECORDS set idstatus = '3' where idserver in (
select idserver from TBL_RECORDS where bkp_date = '2022-07-13' and idstatus = '3')


update TBL_RECORDS set idstatus = '1' where idserver in (
select idserver from TBL_RECORDS where bkp_date = '2022-07-13' and idstatus = '1') and bkp_date = '2022-07-11'

update TBL_RECORDS set idstatus = '2' where bkp_date between '2022-07-17' and '2022-07-17'



select * from TBL_RECORDS where bkp_date between '2022-07-19' and '2022-07-19'
