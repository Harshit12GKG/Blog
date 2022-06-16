function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if(username == '' || password == ''){
        alert('Please enter your username and password')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf,
        },
        'body' : JSON.stringify(data)

    }).then(result => result.json())
    .then(response => {
        if(response.status == 200){
            window.location.href = '/'
            alert("Login Successfully")
        }else{
            alert(response.message)
        }
    })
}

function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value

    if(username == '' || password == ''){
        alert('Please enter your username and password')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/register/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf,
        },
        'body' : JSON.stringify(data)

    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
            window.location.href = '/register'
            alert("Mail Sent Successfully! Check Your Email Id!")
            console.log("Mail Sent Successfully!")
        }else{
            alert(response.message)
        }
    })
}