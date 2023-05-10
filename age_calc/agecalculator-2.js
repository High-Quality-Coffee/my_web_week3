let el=document.getElementById("birthday");
let elResult=document.getElementById("result");
let elSubmit=document.getElementById("submit");

const today = new Date();

function calculateAge(){
    let birthdDate=new Date(el.value);
    let age;
    if(today.getMonth()>birthdDate.getMonth() || 
    (today.getMonth()==birthdDate.getMonth() && today.getDate()>birthdDate.getDate())){
        age=today.getFullYear()-birthdDate.getFullYear();
    }
    else{
        age=today.getFullYear()-birthdDate.getFullYear()-1;
    }
    
    elResult.innerText=`귀하의 만 나이는 ${age} 입니다.`;
    
    return age;
}

elSubmit.addEventListener('click',calculateAge);
