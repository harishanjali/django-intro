document.querySelector('#myform').addEventListener('submit',validate)

function validate(event){
    let v1,v2;
    v1 = parseInt(document.querySelector('#v1').value);
    v2 = parseInt(document.querySelector('#v2').value);
    console.log('submitted')
    if(v1<0 || v2<0){
        event.preventDefault();
    }
}