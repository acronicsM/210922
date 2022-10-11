import React from 'react';


const TodoItem = ({todo}) =>{
    return(
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.activ}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const TodoList = ({todos}) =>{
    return(
        <table>
            <th>Project</th>
            <th>text</th>
            <th>date_create</th>
            <th>date_update</th>
            <th>activ</th>
            <th>user</th>
            {todos.map((todo_) => <TodoItem todo={todo_} />)}
        </table>
    )
}

export default TodoList