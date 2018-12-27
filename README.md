# sysctl.conf 파일 보호 모듈
<hr/>
Copyright 2018, Made By Misty; 한국인터넷진흥원 KUCIS
<hr/>

## Fox_NetSec을 만든 계기
#### Linux/Unix 시스템에서는 일반적인 네트워크 공격들을 방어할 수 있는 수준의 설정값을 지원합니다.

```
sysctl은 kernel parameter값들을 조절하기 위한 utility 입니다.

모든 종류의 네트워크 공격에 대한 방어는 아니지만, well known networking attack의 경우
--> (ICMP redirect, SYN spooffing, deny ping, ignoring broadcasts ping request...~)

/etc/sysctl.conf 경로에 위치한 sysctl.conf 파일의 커널 파라미터 설정값을 통해 막을 수 있는 경우가 많습니다.
많은 서버 보안에 종사하시는 분들이 먼저 회사의 서버를 처음 잡고나서 일반적인 서비스들이 안정화되면,
여러가지 해킹 공격에 대응하려고 노력하기 마련입니다.
그 중, sysctl 파일의 보안 코드 설정은 리눅스 초기 보안 작업 중 아주 중요한 작업 중 하나이죠.
다들 아시다 시피 이 작업은 상당히 귀찮습니다. vi나 leafpad로 열어서 하나하나 작성해야하며, 게다가 오타가 난다면 작동하지 않는 코드가 되버리죠.
그래서 제작하게 된 것이 바로 이 녀석, Fox_NetSec입니다.
```
<hr>

## Fox_NetSec 보안 스크립트를 사용하면 좋은 장점
```
1. 해당 보안 설정 값을 저장한 파일의 유무를 확인하여 관리자에게 통지한다.
2. 귀찮고 반복적인 커널 파라미터 보안 설정값 입력을 자동화 해준다.
3. 안전하고 정확한 보안코드를 입력하되, 해당 코드가 이미 존재한다면 다른 네트워크 공격을 막기 위한 코드가 작성된다.
4. 사용하기가 아주 쉬움. 단순하게 파이썬2만 있으면 끝.
5. 커널 보안 파라미터 설정 뿐만 아니라, 서버를 운영하면서 system performance에 도움되는 설정값도 자동으로 적용.
```


## 다음과 같이 실행할 수 있습니다!!
```
root# python Fox_NetSec.py
```

## 수정이 필요합니다!
```
수정이 필요한 부분이 2곳 존재합니다.
테스트를 위해 filename의 변수 내용을 제 시스템 경로인 /home/foxwomb/projects/sysctl.conf의 경로로 설정되어 있습니다.
해당 2개 경로만 /etc/sysctl로 바꿔주시면 되겠습니다.
```


## 업데이트
#### 2018.12.27일자 업데이트 [내용은 아래와 같음.]
'''
신규 커널 파라미터 설정값 추가

### network hacking protection kernel parameter setting values
1. Enables source route verification
2. Disables automatic defragmentation (needed for masquerading, LVS)
3. Disables the magic-sysrq key
4. Disable ICMP Redirect Acceptance
5. Enable bad error message Protection
6. Enable IP spoofing protection

### Server maintance/performance improving setting values
7. Log Spoofed Packets, source Routed Packets, Redirect packets
8. Improve file system performance
9. Improve virtual memory performance
10. Allowed local port range
11. Improve the number of open files

'''
