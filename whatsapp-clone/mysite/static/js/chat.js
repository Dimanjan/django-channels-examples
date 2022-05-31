const id=JSON.parse(document.getElementById('json-username').textContent);
const message_username=JSON.parse(document.getElementById('json-message-username').textContent);

let url=`ws://${window.location.host}/ws/${id}/`;
let socket=new WebSocket(url)

socket.onopen=function(e){
    console.log('Connection established')
}

socket.onclose=function(e){
    console.log('Connection closed')
}

socket.onerror=function(e){
    console.log('Error',e)
}

socket.onmessage=function(e){
    console.log('Message received',e.data)
    const data=JSON.parse(e.data)

    if (data.username==message_username){
        document.getElementById('chat-body').innerHTML+=
        `<tr>
        <td>
            <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">
                ${data.message}
            </p>
        </td>
        </tr>`
    }
    else{
        document.getElementById('chat-body').innerHTML+=
        `<tr>
        <td>
            <p class="bg-primary p-2 mt-2 ml-5 shadow-sm text-white float-left rounded">
                ${data.message}
            </p>
        </td>
        </tr>`
    }
}

document.querySelector('#chat-message-submit').onclick=function(e){
    e.preventDefault()
    const message=document.getElementById('message_input').value;
    const data={
        username:message_username,
        message:message
    }
    socket.send(JSON.stringify(data))
    document.getElementById('message_input').value=''
}