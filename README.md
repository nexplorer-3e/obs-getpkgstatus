#### 功能 
抓取 obs 中指定的 project repo 的所有软件包的revision，以及其在指定仓库下的构建结果，生成 csv
crawl every package status for every arch in specific repo & project. no need to login.

#### 使用方法
1.  执行pip install -r requirements.txt安装执行该脚本所需的python第三方库
2.  在para.py文件中设置以下参数
 
    ````
    projRepoUrl = {
    "openEuler_2209": "https://build.tarsier-infra.com/project/monitor/openEuler:22.09",  # example
    "<repoName>": "<ProjectMonitorUrl>"
    ````
    <repoName> 是 project monitor 页面上 Repository 里的选项

    <ProjectMonitorUrl> 是 project 里 monitor 选项卡的 url
    
3. 执行python main.py运行脚本，会在脚本所在目录生成obs_pkginfo