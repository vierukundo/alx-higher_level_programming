document.addEventListener("DOMContentLoaded", function() {
      document.getElementById('add_item').addEventListener('click', function() {
        let li = document.createElement('li');
        li.textContent = 'Item';
        document.querySelector('ul.my_list').appendChild(li);
      });

      document.getElementById('remove_item').addEventListener('click', function() {
        let list = document.querySelector('ul.my_list');
        if (list.lastChild) {
          list.removeChild(list.lastChild);
        }
      });

      document.getElementById('clear_list').addEventListener('click', function() {
        document.querySelector('ul.my_list').innerHTML = '';
   });
});
