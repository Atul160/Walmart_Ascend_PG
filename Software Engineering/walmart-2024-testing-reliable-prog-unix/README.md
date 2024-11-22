# walmart-2024-testing-reliable-prog-unix


## reliable programming 
- retrospective from reliable programming 
- different metrics on the code which can be measured 
- whether its good code or not 
- code to be less complexity, should have the standards
- proper commenting 
- we should be writing efficient code 
- system will be able to understnad but we need to write human readable code 
- code to be reusable, should be classified 
- TIOBE Tics for coding standards - https://www.tiobe.com/coding-standards/
- FMEA - Failure Mode & Effective Analysis 




##  Topics for coverage - 09-Aug-2024 

- Introduction to Manual Testing 
- Introduction to Automation testing
- Software Test Levels
- Software Test Types (1. Functional 2. Non-Functional)
- Software Test Process / STLC
- Software Quality Standards
- Performing White Box/Black Box/Grey Box Testing
- Identify the bug



- SDET 
- Waterfall - Project
    - Developer 
        - Java 
        - .Net
        - Pascal
        - Cobol 
    - Tester 
    - QA 

- Agile - Product  
    - Sprint Based - 14 Days, 21 Days etc 
    - Tangible output which has to come with in stipulated time 
    - SDET - Software Developer Engineer & Tester 
    - VModel 
        - MDD - Model Driven Development 
        - DDD - Domain Driven Development 
        - BDD - Behaviour Driven Development 
            - Given When Then And But 
        ```
            Scenario: to add 2 numbers 
            AC 1: 
                Given the application is working fine 
                When the user enters the number to add 10 and 20 
                Then the application should return value 31 

            AC 2: 
                Given the application is working fine
                Whent he user enters the number to add 10.0 and 20.4 
                Then the application should return 30.4 
            AC 3: - failed case 
                Given the application is working fine
                Whent he user enters the values to "hi" and "bye" to add 
                Then the application should return HELLO


            Scenario: to divide 2 numbers 
            AC1: 
            AC2:
            AC3: 
        ```

            AC1 : passed case.

            Given the application is working fine 
            When user enteres the number to divide 50 and 25 
            Then the application should return 2

            AC 2 : 
            Given the application is working fine.
            When user enteres the number to divide 0 and 100
            Then the application should return 0

            AC 3
            Given the application is working fine.
            When user enteres the number to divide 25 and 0
            Then the application should return error



        - TDD - Test Driven Development - Lowest Level

- Types of Testing 
    - White Box 
    - Grey  Box 
    - Black Box 


```
    - to add 2 numbers 

    int add(int num1, int num2) {
        return num1 + num2; 
    }

    T add (T1 num1, T2 numb2) {
        return num1 + num2; 
    }
    int add(double num1, double num2) {
        return num1 + num2; 
    }

    int add(byte num1, byte num2) {
        return num1 + num2; 
    }

```


## Types of testing 

### Functional Testing 
    - Unit Testing 
    - Integration Testing 
    - System Testing 
    - UAT (User Acceptence Testing)
    - Regression Testing 
    - Smoke Testing 
    - Sanity Testing 
### Non-Functional Testing
    - Performance Testing 
        - Load Testing 
        - Stress Testing 
        - Spike Testing 
        - Scalable Testing 
        - Volume Testing 
    - Security Testing
        - Infrastructure 
        - Application 
        - Cloud 
        - Network
    - Usability Testing 
    - Compatability Testing  
    - Localization Testing 
    - Compliance Testing 
    - Recovery Testing 
### Other Types of Testing 
    - Alpha Testing 
    - Beta Testing 
    - Ad-hoc Testing 
    - Exploratory Testing 
    - End-To-End 
    - A/B Testing 
    - Databases Testing 
 
### What the heck is this 
- Error - which produces incorrect output / result - happens by human 
- Bug - its an error which be identified only upon execution 
- Fault - state of error 
- Failure - the software is not performaing as expected, at the particular time 


## 10-Aug-2024
- Mocking the tests - TDD 
- 7 types of security testing 
    - Vulnerability Scanning  
        ```
            lang=en
        ```
    - Pen Testing (Penetration)
    ```
        public boolean insertEmployee(int empId, String name) {
            String sql ="insert into employee values(?,?)"; 

            GetConnection gc = getMysqlConnection(); 
            PreparedStatement = gc.preparedStatement(sql); 
            ... 
        }
    ```
    - Security Audits 
    - Risk Assessment 
    - Ethical Hacking 
    - Security Assessment 
    - Red Teaming 
- Myths and facts about security Testing 
- Performing Code reviews - Git



```
    - standards 

    public interface Device {
        public void on();
        public void off();
    }
    - blr 
        class AC implements Device{
            public void on() {..}
            public void off() {..}
        }
    - chn 
        class Projector implements Device {
            public void on() {..}
            public void off() {..}
        }
    - del 
        class Monitor implements Device{
            public void on() {..}
            public void off() {..}
        }
    - Hyd 
        class Remote{
            public void on(Device d){
                d.on()
            }
        }

```




### ways of working with java 
1. You create an object 
    ```
        EmployeeDAOMySQL dao = new EmployeeDAOMySQL(); - but this code is tighly coupled to particular class 
        EmployeeDAOOracle dao1 = new EmployeeDAOoracle(); 
    ```

2. better way 

```
    IEmployeeDAO dao = new EmployeeDAOMySQL(); 
    dao = new EmployeeDAOoracle(); 
```
3. mock way 

```
    IEmployeeDAO dao = mock(IEmployeeDAO.class); -> behind the screen mockito creates an object of interface and keep it handy 

```







# 23-aug-2024 
## Session 1 

- Why UNIX?
- Variants of Unix Operating System
- Unix Operating System Concepts 
- (Multiuser, Multitasking ,Multiprocessing)
- The UNIX Operating System  Architecture 
- (H/W , Kernel , Shell  and Other Applications)
- Unix Directories Structure (bin, usr, etc, home, dev, var, tmp)
- Files and inodes (detailed specification of inode table)
- Logging in (Terminal Type, Passwords, Exiting, Identity)
- Unix Command Line Structure
- Control Keys
- Getting help
- Directory Navigation and Control 
- (pwd,cd, mkdir, rmdir, ls)
- File Maintenance Commands (cp, mv, rm)
- File Permissions with options, chmod, chown, chgrp, ls
- Understanding based on Permissions
- Display Commands 
- (echo, cat, more, less, and pg - page through a file, head, tail)
- Working With Files (cmp, diff, cut, paste - merge files, touch - create a file ,wc, Softlink and - harlinks using ln- link to another file , sort, tee, uniq, strings, file – file type, tr)


- you need to have linux box or git bash
## Features of Unix 
    - Memory Managament - Chache Memory, Primary Memory, Secondary Memory 
    - Multi Tasking 
    - Multi User 
    - Time Sharing System 
    - File Management 
    - Input / Output connectin devices 
    - Security 
    - Communication & Networking 
    - Unix building utilities & softwares 
        - CLI OS 
        - Linux 
        - MAC
        - sun solaris... 

## Programming practice 
- Multi Threads - are controllect in a program 
- quantum time - will exeucted in RR, Priority First Scheduling  
- System call - an instruction sent to kernel, routine stored in kernel 
    - File maniuplation 
    - process control 
    - information retrieval 
    - smallest work which happens in the system 
    - read 



```
- rw- r-- r--   (- represents its ordinary file )
d rwx r-x r-x   (d represents its a direcroty file)


rw- - User 
r-- - group 
r-- - others 

```


- wild card characters 
- Different types of shell - sh, bash, ksh, csh 



## Session 2 
- Different Types of shells
- Customizing the shell environment (.profile,rc file)
- Environmental Variables
- Escaping and Quoting
- Variables (system and user defined variables)
- Control Statement (test specifications need to be additionally discussed)
- Looping
- Functions
- Here Document (<<)
- Parsing Files with read operations
- Overview to connect to sqlplus and run simple queries
- Calling C++ applications and Java specifications via Unix





- working with variables - exporting 

```
    > mvn - the system defaultly checkeks if the file exists in the current folder 
    > mvn - it will check if there is variable set 
    > mvn - set this variable at the .bash_profile or to your shell specific 
```

- IO Redirection 
```
    - < for input redirection (any input from keyboard shall be given here )
    - > output redirection (by default is on console but can be put on file)
    - >> apprending redirection (appends the content to the file)
```


- chmod 
```
    - octa series (0-7)
    - owner - Read(4) Write(2) Execute(1)
    - group - Read Write Execute 
    - other - Read Write Execute 


    - rw- r-- r--  1 naveenkumar  admin   31 Aug 23 12:50 hello.txt


    - u, g, o 
    - + or - 
    - r, x, w 

    - defult - 644 
```



- if else - else if 

- accept user state if the user is from karnataka then welcome to karnataka - some text 
- accept user state if the user is from Maharastra then welcome to maharastra - some text 
- else you are from other state 



- excersice - accept 2 file names from the application, the first name (file name) should be there in the path specified, if found then copy the file to second file name 


> hello.txt  (-f -a number of chars more than 0 -s) true copy the file in  
> sample.txt 

# 30-aug-2024 

- What is a Version Control System (VCS)?
- Distributed vs Non-distributed VCS
- What is Git and where did it come from?
- Git commands (Clone, Working Tree, Checkout, Staging area, Add, Commit, Push, Pull)
- Creating a repository (git init)
- Checking status (git status)
- Adding files to a repository (git add)
- Committing files (git commit)
- Removing staged files (git reset)
- Push repository to github performing PR
- Branching Strategy + Mono Repo 


## in the class 
- its the repo to store your code 
- gives capabilities to create branches 
- VCS 
- you can maintain the local copy 
- access from anywhere 
- helps collaborate 
- tracking the development progress 


ssh-keygen -t ed25519 -C "adith.naveen@gmail.com"


```
    > git clone https://github.com/adithnaveen/Walmart-git-training-delete.git - this command shall give all the code + branches associated 

    > 
```


# 03-sep-2024 

## ELK 

- prometheus + Grafana 
- grafana vs kibana 
- newrelic 

- telemetrics 
    - system 
        - i've 3 instances of login service 
        - i've 4 instances of accounts service 
        - ..... 
    - system break down /slow/ reaching saturation /... 
    - business 

- Elastic
- Kibana
- Logstash 

## setup elk with docker compose 

```
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - xpack.security.enabled=false
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"

  kibana:
    image: docker.elastic.co/kibana/kibana:7.15.0
    ports:
      - "5601:5601"
    environment:
      ELASTICSEARCH_HOSTS: "http://elasticsearch:9200"
    depends_on:
      - elasticsearch

  logstash:
    image: docker.elastic.co/logstash/logstash:7.15.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch

volumes:
  esdata:
    driver: local

```

> docker ps 

> docker images 


> docker-compose up -d  -- to start the service in deamon 

> docker-compose down -- to shut down 



- to list the indices in verbose mode - GET 
> http://localhost:9200/_cat/indices?v

> http://localhost:9200/_cat/indices?h=uuid,docs.count

```
 <iframe src="http://localhost:5601/goto/6bbff7b985a4cb30f369943c667a1b5e" height="600" width="800"></iframe>
```
- can give it to front end application 



# 13-sep-2024 
JavaScript Day 1

- Basics of Javascript
- JavaScript Introduction
- Building blocks of Javascript
- JavaScript Objects	
- Javascript Object oriented programming
- Creating objects in Javascript
- Defining method in Javascript object 


## front end team 
- builds front end application 
- RIA 
- pls ensure to have the contract with the backend team - data model 




```
    {
        var xx;  - should i use this + at what level 
    }
    {
        let x; 
    }

```


### Differenciate React v/s MERN 
- react is the front end library 

- UML 
    - use Case 
    - sequence 
    - flowchart 

- screens 
- swagger document 

```
{
    username:"Naveen", 
    email:"naveen@naveen.com", 
    dob:"1-1-1990"
}
```


# 14-sept-2024 


## JavaScript Day 2	

- Nested Object-Aggregation
- Prototypal Inheritance, Constructor Pattern
- Polymorphism in Javascript
- Javascript Functions, Output, Array, Strings, Date
- Javascript Number & Math Objects Scope
- Scope and the Javascript Compiler
- Compiling Function Scope, Execution of Function Code
- Function Declarations, Function Expressions
- Block Scope, Dynamic Scope




- Writing simple javascript program 
- writing javascript .js file and invoking in html 
- you can have .js, .css files seperated from .html 

### good to use scope of variable 
    - const 
    - let 
    - var 
    - global variable 


###  in java script there is no class, function itself is treated as class 

- prototype equivalent in java 


```
    class Person {
        int age; 
        String firstName; 
        String lastName; 

    public void display () {
        System.out.println("Age is " + age); 
        System.out.println("FirstName is " + firstName); 
        System.out.println("lastName is " + lastName); 
    }

    }
```

- splice 

```
    splice(indexPosition, noOfElementsToBeDeleted, [rest of elements to be added]);
    Ex: 
    splice(1,2,3);  - goto index 1, delete 2 values, add value 3 
    splice(3,0,2,3,4,5,6,7); go to index 3 dont delete any value then add rest of it 
    splice (2,1); goto index 2 and delete 1 value 

```

## associative arrays 
- in javascript the values to the functions are passed as associative arrays 
- so there is no concept of function overloading 


# 18-sep-2024 


## AOT v/s JIT 
- AOT will compile the code at build time - time is the concern, we need less time to execute the code. 
- JIT will compile the code at run time
- we live in the world of polyglot - my programming language is java, python, javascript, c++, go etc.. 
- c++ vs java - the faster is always c++, is c++ executes in native system 

```
-- million iterations code with JIT 
Total Tim For iteration is :374404775
java com.naveen.StressTest  0.50s user 0.17s system 111% cpu 0.596 total


-- million iterations code with AOT - Graal 
Total Tim For iteration is :54
./com.naveen.stresstest  0.00s user 0.00s system 71% cpu 0.012 total 
```

# 20-sep-2024 


JavaScript Day 3

- Closures
- Browser Object Model
- Window Object
- History Object
- Javascript Form Validations
- Form Validations
- Email Validations"


```

    ( /     [^\s@]+   @     [^\s@]+\.[^\s@]+     /    );


http://127.0.0.1:5500/java-script-works/registration/Registration.html?

userName=kumarnaveen&
usrPwd=kumar%401234&
cpwd=kumar%401234&
sex=m&
qual=bsc&
addrs=teseolkjsdflkjsldkfjlksjdf+ljsld+fjlkjsdfsdf&
country=india&
cb1=sports&
cb2=politics&
terms=A&
regbtn=Register

```


# 21-sep-2024 

## working with es6 
```
[Arguments] 

{ 
    '0': [ '', ' is ', ' old' ],  - string 
    '1': 'Diwya', - first template substition 
    '2': 30 - second template substition 
}
```



## introduction to reactjs 

```
- frament 2 
        <fragment2> 
            <div></div>
        </fragment2>

- fragment 1
    <>
        <fragment2/> 
        <div></div>
        <div></div>
    </>


// stateful component 
class HelloWorld extends Component {
     render() {
        return <></>
    }
}


// stateless component 
const HelloWorld = () => {
    return null; 
}; 


<App>
    <div>
        <Header title="This is my React Application"/>
    </div>
</App>


class Header extends React.Component {
    render() {
        return 
        <div>
            <h1>{this.props.title}</h1>
            <hr />
            <h2>This another tag</h2>
        </div>
    }
}

const Header = (props) => {
    return <div>
     <h1>{title}</h1>
    </div>
}
```

```
> npm i -g react react-dom --save

-- to check the list of packages installed 
> npm list 

-- to create react application 
> npx create-react-app react-demo-1

-- to start reactjs application 
> npm start 
```

### once after react application is generated 

```
Success! Created react-demo-1 at /Volumes/Kanchan/MyTrainings/walmart/walmart-2024-testing-reliable-prog-unix/react-works/react-demo-1
Inside that directory, you can run several commands:

  npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd react-demo-1
  npm start

```

- understand concepts first 
- yesterday program is was too much -like export 
```
business-logic.js - Diwya 
    let func = (a) => a + a
    let obj = {}
    let x = 0


--------------------------

app-development.js - sudarshan 
import func from './business-logic.js' 

let mymaths = (num) => func(num); 


```
- why you are trying to do in index.js 
- why are you giving in ./ 
- why app-header,app-footer, why app-content etc why 

```

    int maths (int num1, int num2, String opr) {
        if(opr.equals("add")) {
            return num1 + num2; 
        }else if(ops.equals("sub")) {
            return num1 - num2;
        }.......
    }

    - is more of cohesive  
    int add(num1, num2) {
        return num1 + num2; 
    }

    int sub(num1, num2) {
        return num1 - num2; 
    }



    // implementing reactjs application without cohesiveness 



    import React, {Component} from 'react'; 

    
    class App extends Component{
        constructo() {}

        render() {
            let company="Walmart";
            let year = 2024; 
            let website="http://walmart.com";

            <div>
                <div className="app-header">
                        <h1>{company}</h1>
                </div>
                <div className="app-content">
                    <h2>This is content page 
                </div>
                <div className="app-footer">
                    <p> this is footer {year} wesite is {website}
                </div>

            </div>
        }
    }

- http://somesite.com/api/customers - GET 

```


- doing assignment is difficult 

# 28-sep-2024 

- Handling - bind function 
```
    <div>
        <h1></h1>
    </div>

    <Fragment>
        <h1></h1>
    <Fragment/>
```
- event handler with  stateful (class) component + stateless (function) component 
- create the form using uncontrolled way (old)
- form with controlled component 
- form validation 
- life cycle function 

# 04-oct-2024 

```
    - life cycel 

- MyComponent - will have the properites of Component class 
    class MyComponent extends React.Component  {

        constructor() {
            super();
        }
        // lifecycle 
    }
```
- working with arrays
- fetch data from external api and show in react component 
- HOC 

# 05-oct-2024 

```
- regular style = 
let contacs = new Array(6);
contacs.map(function(c){
    return <ContactCard contact={c} key={c.id} />
})

- json-server --watch data.json 
- npm i json-server -> this will make an enty in package .json 
- npm num rest-server 

- arrow style    contacts.map(c => <ContactCard contact={c} key={c.id} />)
```


- React with Redux 
```
    - data store will be in store 
    - action 
        - let action = {type:'INSERT', payload:"{name:'naveen', email:'naveen@gmail.com}"}
        - let action = {type:'FETCH'}
        - let action = {type:'UPDATE', payload:{id:101, name:'naveen kumar'}}
        store.dispatch(action); 

        - npm i bootstrap redux react-redux redux-devtools-extension redux-thunk json-server
        - npm i --force bootstrap redux react-redux redux-devtools-extension redux-thunk json-server
```
- Routing 
- Lazy Loading 
- Error handling 
- react Hooks 
- react hooks + retrieving data 



 ## Resources 

- https://www.w3.org/WAI/WCAG2AAA-Conformance
- https://gdpr-info.eu/art-23-gdpr/
- https://github.com/settings/tokens
- https://www.graalvm.org/latest/getting-started/ - graal vm tutorial getting started
- https://compat-table.github.io/compat-table/es6/ 
- https://redux.js.org/tutorials/fundamentals/part-2-concepts-data-flow#reducers - redux flow 

