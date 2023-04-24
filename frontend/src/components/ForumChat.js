import React, { Component } from 'react';
import { List, ListItem, ListItemAvatar, ListItemText } from '@mui/material';
import { styled, Typography, Box, Container, TextField, Button, Stack} from '@mui/material';
import { AccountCircle } from '@mui/icons-material';
import SendOutlinedIcon from '@mui/icons-material/SendOutlined';

const CustomBox = styled(Box)(({theme}) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
  borderRadius: '5px',
}));

const CustomListItemText = styled(ListItemText)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));

const CustomAccountCircle = styled(AccountCircle)(({ theme }) => ({
  color: theme.palette.surface.text,
}));


const CustomTextField = styled(TextField)(({ theme }) => ({
  backgroundColor: theme.palette.surface.variant,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
  width: '85%'
}));

const AddButton = styled(Button)(({theme}) => ({
  width:'15%',
  height: '100%'
}));



class ForumChat extends Component {
  state = {
    title: '',
    content: '',
    author: '',
    chatPosts: [['Title1', 'Content1', 'Author1'], ['Title2', 'Content2', 'Author2']]
  }
  render() {
    //States 
    const title = this.state.title;
    const content = this.state.content;
    const author = this.state.author;
    const setTitle= (params) => this.setState({ title: params });
    const setContent= (params) => this.setState({ content: params });
    const setAuthor= (params) => this.setState({ author: params });
    const chatPosts = this.state.chatPosts;
    const setChatPost= (params) => this.setState({ chatPosts: params});

    const addPost = () => {
      setChatPost([...chatPosts, [title, content,author]]);
      setTitle('');
      setContent('');
      setAuthor('');
    };
    function noContent(content) {
      if(content !== ''){
        return <AddButton variant='contained' color='success' onClick={addPost}><SendOutlinedIcon></SendOutlinedIcon></AddButton>
      }else{
        return <AddButton variant='outlined' color='success' disabled><SendOutlinedIcon></SendOutlinedIcon></AddButton>
      };
    };
    return (
      <>
      <Container maxWidth='xl'>
        <CustomBox>
          <List>
            {chatPosts.map(post => (
              <ListItem>
                <ListItemAvatar><CustomAccountCircle/></ListItemAvatar>
                <CustomListItemText primary={post[0]} secundary={
                  <React.Fragment>
                    <Typography
                      sx={{ display: 'inline' }}
                      component="span"
                      variant="body2"
                      color="text.primary"
                    >
                      {post[2]}
                    </Typography>
                    {"--" + post[1]}
                  </React.Fragment>
                }/>
              </ListItem>
            ))}
          </List>
          <Stack direction='row' justifyContent='space-evenly' alignItems='center'>
            <CustomTextField variant='outline' label='Post' placeholder='Enter text here' color='success' value={content} onChange={event => setContent(event.target.value)}></CustomTextField>
            {noContent(content)}
          </Stack>

        </CustomBox>
      </Container>
      </>
    )
  }
}
export default ForumChat;