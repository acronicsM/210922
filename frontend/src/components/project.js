import React from 'react';
import {Link} from 'react-router-dom';


const ProjectItem = ({project}) =>{
    return(
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>{project.link}</td>
            <td>{project.users}</td>
             <td>
                <Link to={`/projects/${project.id}`}>task list</Link>
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) =>{
    return(
        <table>
            <th>Project name</th>
            <th>Link</th>
            <th>users</th>
            <th>todo</th>
            {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectList