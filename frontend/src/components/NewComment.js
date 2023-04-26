import {React, useState} from 'react';
import {Dialog, DialogActions, DialogContent,DialogContentText, DialogTitle} from '@mui/material';
import {styled, Button,TextField, Grid} from "@mui/material/"
import SendOutlinedIcon from '@mui/icons-material/SendOutlined';

const CustomDialogContentText = styled(DialogContentText)(({ theme }) => ({
  color: theme.palette.surface.main,
  backgroundColor: theme.palette.surface.main,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}));

const CustomDialogTitle = styled(DialogTitle)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}
));

const CustomDialogContent = styled(DialogContent)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}
));

const CustomDialogActions = styled(DialogActions)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}
));

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

function PostComment(props) {
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [user_id, setUser_id] = useState(JSON.parse(sessionStorage.getItem('user')).user_id); 
  const [created_at, setCreated_at] = useState(new Date().toISOString()); 
  const parent_post_id = props.post_id; 
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
      .then(data => console.log(data))
      .catch(error => console.error(error));
    
    handleClose();
    window.location.reload();
  };

  function noInput(input1, input2) {
    if(input1 !== '' && input2 !== ''){
      return <AddButton variant='contained' color='success' autoFocus onClick={handleSubmit}><SendOutlinedIcon></SendOutlinedIcon></AddButton>
    }else{
      return <AddButton variant='outlined' disabled><SendOutlinedIcon></SendOutlinedIcon></AddButton>
    };
  };

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <>
      <Button variant="text" size="medium" onClick={handleClickOpen}>
        comment
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="comment-dialog-title"
        aria-describedby="comment-dialog-description"
      >
        <CustomDialogTitle id="comment-dialog-title">
          {"New Comment"}
        </CustomDialogTitle>
        <CustomDialogContent>
          <CustomDialogContentText id="comment-dialog-description">
            <Grid container spacing={1}>
              <Grid item xs={12}>
                <CustomTextField id='title' label='Post Title' variant='filled' value={title} onChange={event => setTitle(event.target.value)}/>
              </Grid>
              <Grid item xs={12}>
                <CustomTextField id='content' label='Post Content' variant='filled' multiline value={content} onChange={event => setContent(event.target.value)}/>
              </Grid>
            </Grid>
          </CustomDialogContentText>
        </CustomDialogContent>
        <CustomDialogActions>
          <AddButton variant='Text' onClick={handleClose}>Close</AddButton>
          {noInput(title, content)}
        </CustomDialogActions>
      </Dialog>
    </>
  );
};

export default PostComment;