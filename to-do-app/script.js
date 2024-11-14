// Add new task on button click or Enter key press
function add() {
  const input = document.getElementById('input-item');
  const task = input.value.trim();

  if (task) {
      const li = document.createElement('li');
      li.innerHTML = `${task} <button class="delete-btn" onclick="deleteTodo(this)">❌</button>`;
      document.getElementById('list').appendChild(li);
      saveTasks();  // Save tasks after adding
      input.value = '';
  }
}

// Delete a task
function deleteTodo(button) {
  const li = button.parentElement;
  document.getElementById('list').removeChild(li);
  saveTasks();  // Save tasks after deletion
}

// Save tasks to localStorage
function saveTasks() {
  const list = document.getElementById('list');
  const tasks = Array.from(list.children).map(li => li.textContent.trim().slice(0, -1));
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Load tasks from localStorage on page load
function loadTasks() {
  const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
  tasks.forEach(task => {
      const li = document.createElement('li');
      li.innerHTML = `${task} <button class="delete-btn" onclick="deleteTodo(this)">❌</button>`;
      document.getElementById('list').appendChild(li);
  });
}

// Add task on Enter key press
document.getElementById('input-item').addEventListener('keypress', function(e) {
  if (e.key === 'Enter') add();
});

// Load tasks on page load
window.onload = loadTasks;
