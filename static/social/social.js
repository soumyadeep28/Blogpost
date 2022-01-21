
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  
function Likepost(postid) {
    return fetch('/post/'+ postid +'/like',
    {
        method : 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
          }

    }).then(() => {
        window.location.reload()
    })
}

function Commentpost(postid ,comment) {
    const formdata = new FormData()
    formdata.append('content' , comment)
    return fetch('/post/'+ postid +'/comment',
    {
        method : 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
          },
        body: formdata

    }).then(() => {
        window.location.reload()
    })
}