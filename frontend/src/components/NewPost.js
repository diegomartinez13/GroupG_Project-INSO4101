import React, { useState } from 'react';
import {styled, Button,TextField, Grid} from "@mui/material/"
import SendOutlinedIcon from '@mui/icons-material/SendOutlined';


const CustomTextField = styled(TextField)(({ theme }) => ({
  backgroundColor: theme.palette.surface.variant,
  color: theme.palette.surface.text,
  '& .MuiInputBase-input, & textarea': {
    color: theme.palette.surface.text,
  },
  '& .rbc-event': {
    backgroundColor: theme.palette.surface.main,
    color: theme.palette.surface.variant,
    '& .MuiInputBase-input, & textarea': {
      color: theme.palette.surface.variant,
    },
  },
  width: '100%',
}));

const AddButton = styled(Button)(({theme}) => ({
  width:'25%',
}));



function PostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [user_id, setUser_id] = useState(JSON.parse(sessionStorage.getItem('user')).user_id); 
  const [created_at, setCreated_at] = useState(new Date().toISOString()); 
  const [parent_post_id, setParent_post_id] = useState(null); // null parentPost means it is a new post with no parent
  const URL_POST = 'http://localhost:5000/posts';

  function handleSubmit(event) {
    event.preventDefault();
    console.log(title, content, user_id, created_at, parent_post_id);
    const data = { title, content, user_id, created_at, parent_post_id };
    
    fetch(URL_POST, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        window.location.reload();})
      .catch(error => console.error(error));
    
    
  };

  function noInput(input1, input2) {
    if(input1 !== '' && input2 !== ''){
      return <AddButton variant='contained' color='success' onClick={handleSubmit}><SendOutlinedIcon></SendOutlinedIcon></AddButton>
    }else{
      return <AddButton variant='outlined' disabled><SendOutlinedIcon></SendOutlinedIcon></AddButton>
    };
  };

  return (
    <Grid container spacing={1}>
      <Grid item xs={6}>
        <CustomTextField id='title' label='Post Title' variant='filled' value={title} onChange={event => setTitle(event.target.value)}/>
      </Grid>
      <Grid item xs={12}>
        <CustomTextField id='content' label='Post Content' variant='filled' multiline value={content} onChange={event => setContent(event.target.value)}/>
      </Grid>
      <Grid item xs={12}>
        {noInput(title, content)}
      </Grid>

    </Grid>
  );
}

export default PostForm;