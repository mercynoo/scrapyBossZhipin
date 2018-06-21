-- create database zhipin DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use zhipin;
CREATE TABLE 产品 (
    id INTEGER(100) AUTO_INCREMENT PRIMARY KEY ,
    company VARCHAR(100) NOT NULL ,     # 公司名字
    positionName VARCHAR(100) NOT NULL, # 职位名称
    seniority VARCHAR(150),             # 工作年限
    salary VARCHAR(100),                # 薪资范围
    education VARCHAR(150),             # 教育程度
    city VARCHAR(100),                  # 城市
    industryField VARCHAR(150),         # 行业
    financeStage VARCHAR(150)           # 融资情况
    -- amount VARCHAR(150)                 # 公司人数
)
