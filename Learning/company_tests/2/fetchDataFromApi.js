'use strict';

/* global $, jQuery */

function solution() {
  const basicTemplate = `<div class="comment-item">
                <div class="comment-item__username">{username}</div>
                <div class="comment-item__message">{message}</div>
            </div>
            `;
  let commentLists = document.getElementsByClassName('comment-list');

  for (let i = 0; i < commentLists.length; i++) {
    let dataCount = commentLists[i].getAttribute('data-count');
    commentLists[i].innerHTML = 'Loading...';

    fetch('https://www.example.com/comments?count=' + dataCount)
      .then(resp => resp.json())
      .then(data => {
        let itemHTML = '';
        for (let j = 0; j < data.length; j++) {
          itemHTML += basicTemplate
            .replace('{username}', `${data[j].username}`)
            .replace('{message}', `${data[j].message}`);
        }
        commentLists[i].innerHTML = itemHTML;
      })
      .catch(err => {
        commentLists[i].innerHTML = '';
      });
  }
}
