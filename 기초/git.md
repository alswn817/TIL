# **TIL (Git)**
   ## <span style='background-color: #fff5b1'>**Repository**</span>
       
#### **로컬 저장소(local repository)**   
+ 내 PC에서 관리하는 git 저장소   
#### **원격 저장소(remote repository)**   
+ 로컬 저장소를 업로드 하는 곳. ex) GitHub, Bitbucket, GitLab 등
+ clone 명령어로 기존 원격 저장소를 로컬에 받을 수 있음.   
   
#### **작업 폴더(Working Directory)**   
+ 작업이 일어나는 폴더

#### **Staging Area(Index)**   
+ 작업 폴더에서 작업한 변경 내용을 기록 하는 곳(git 저장소에 commit하기 전에 올려두는 공간)   
+ stage에서 commit을 하게 되면 git 저장소로 변경 내용이 저장됨.  
   ***
   
   
   
   
## <span style='background-color: #fff5b1'>**Git Command**</span>   

#### **stage(Staging Area)**   
+ Staging Area는 Git Directory에 있다.   
+ 곧 commit할 파일에 대한 정보를 저장하는 곳   


#### **status**   
+ 파일의 상태를 확인하는 명령어.   
+ status를 사용하는 예시로는 아래의 코드가 있다.   
`$ git status`

#### **add**   
+ 작업 폴더에서 작업한 변경을 stage에 올릴 때 사용하는 명령어.   
+ add한 파일이 tracked 상태가 됨(git이 관리하는 대상이 됨)   
+ 파일을 지정해서 올릴 수도 있고, 경로를 지정해서 변경된 모든 파일을 올릴 수도 있음.   
+ add를 사용하는 예시로는 아래의 코드가 있다.   
`$ git add 파일 1, 파일 2`   
`$ git add .`   

#### **commit**   
+ git add 명령어로 stage에 추가한 수정 파일을 git 저장소에 저장   
+ 하지만 stage에 올려놓지 않은(untracked) 파일은 commit되지 않는다.   
+ commit을 사용하는 예시로는 아래의 코드가 있다.   
`$ git commit -m "메모할 내용"`   

#### **pull**   
+ 원격 저장소의 데이터를 가져오고, 자동으로 현재 작업하는 로컬 브랜치와 merge한다.   
+ pull을 사용하는 예시로는 아래의 코드가 있다.   
`$ git pull origin master/main`   

#### **push**   
+ commit한 파일을 원격 저장소에 올리는 명령어.  
+ push를 사용하는 예시로는 아래의 코드가 있다.   
```
$ git push
$ git push origin (master/main)
```

#### **fetch**   
+ 로컬에는 없지만 원격 저장소에 올라가 있는 데이터를 모두 가져옴.(업데이트)   
+ 자동으로 merge 작업을 하지는 않는다.   
+ fetch를 사용하는 예시로는 아래의 코드가 있다.   
`$ git fetch origin master/main`   

#### **branch**   
+ 여러 개발자들이 동시에 다양한 작업을 할 수 있게 만들어 주는 기능   
+ 처음으로 저장소를 만들면 git에서 master라는 branch를 가장 처음 만든다.   
+ 필요에 의해 만들어지는 각각의 branch는 다른 branch의 영향을 받지 않는다.   
+ 여러 작업을 동시에 진행할 수 있다.   

#### **clone**
+ 이미 초기화된 원격저장소를 복제해와서 개발하는 경우, 복제 작업을 Git에서는 clone이라고 부름.   
+ clone을 사용하는 예시로는 아래의 코드가 있다.   
`$ git clone [REPO_URL] [DIR]`   

#### **merge**   
+ merge를 사용하여 여러개의 branch를 병합할 수 있다.  
+ 현재 작업 중인 branch에 합칠 commit을 지정해서 병합함.   
+ commit 위치에는 주로 병합할 branch 이름을 넣고, commit checksum을 넣어도 됨   
+ (숫자랑 영어로 조합된 40글자 SHA-1 해시 값, 커밋 고유 번호)  
+ merge를 사용하는 예시로는 아래의 코드가 있다.   
`$ git merge`   

#### **checkout**   
+ branch를 전환한다. ex / master -> main 혹은 main -> master / (다른 branch로도 변경이 가능하다.)   
+ merge를 사용하는 예시로는 아래의 코드가 있다.   
`$ git checkout develop`   