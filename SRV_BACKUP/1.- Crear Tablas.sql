--Crear tabla de Estados
CREATE TABLE TBL_STATES (
id INT not null PRIMARY KEY IDENTITY(1,1),
state_name nvarchar(50) not null,
state_detail nvarchar(100) not null,
active bit not null)

--Crear tabla de Tipos de Servidores
CREATE TABLE TBL_TYPE (
id INT not null PRIMARY KEY IDENTITY(1,1),
typename nvarchar(50) not null,
type_detail nvarchar(100) not null,
active bit not null)

--Crear tabla de dias de Backup
CREATE TABLE TBL_DAYS (
id INT not null PRIMARY KEY IDENTITY(1,1),
day_name nvarchar(50) not null,
day_detail nvarchar(100) not null,
active bit not null)

--Crear tabla de servidores
CREATE TABLE TBL_SERVER (
id INT not null PRIMARY KEY IDENTITY(1,1),
server_name nvarchar(100) not null,
id_type INT not null CONSTRAINT FK_TBLTYPE_ID FOREIGN KEY (id_type) REFERENCES TBL_TYPE(ID),
server_ip nvarchar(30) not null,
bkp_week nvarchar(20) not null,
id_dia INT not null CONSTRAINT FK_TBLDAYS_ID FOREIGN KEY (id_dia) REFERENCES TBL_DAYS(ID),
bkp_start nvarchar(20) not null,
bkp_retention nvarchar(20) default null,
bkp_active bit not null default 1,
active bit not null default 1)

--Crear tabla de registro de Backup
CREATE TABLE TBL_RECORDS (
id INT not null PRIMARY KEY IDENTITY(1,1),
idserver INT not null CONSTRAINT FK_TBLSERVER_ID FOREIGN KEY (idserver) REFERENCES TBL_SERVER(ID),
idstatus INT not null CONSTRAINT FK_TBLSTATES_ID FOREIGN KEY (idstatus) REFERENCES TBL_STATES(ID),
bkp_date datetime not null,
reg_user nvarchar(50) not null,
reg_date datetime default getdate(),
active bit not null)


--eliminar tablas
--drop table [dbo].[TBL_STATES]
--drop table [dbo].[TBL_TYPE]
--drop table [dbo].[TBL_DAYS]
--drop table [dbo].[TBL_SERVER]
--drop table [dbo].[TBL_RECORDS]

--ASIGNAR FOREIGN KEYS
--CONSTRAINT FK_TBL_SERVER_ID_TYPE FOREIGN KEY (id_type) REFERENCES TBL_TYPE(id)