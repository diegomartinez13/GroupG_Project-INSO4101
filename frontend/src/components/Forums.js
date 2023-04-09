import React, {Component} from 'react';
import {styled, Button, Container, TextField, Typography, Stack, Badge} from "@mui/material/"
import {Card, CardContent, CardHeader} from "@mui/material/"
import {List, ListItem, ListItemButton, ListItemIcon, ListItemText} from "@mui/material/"
import {Inbox, MessageOutlined} from '@mui/icons-material/';

const StyledContainers = styled(Container)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
  margin: '0.5rem'
}));

const CustomForumCard = styled(Card)(({ theme }) => ({
  backgroundColor: theme.palette.surface.variant,
  alignContent: 'center',
  justifyContent: 'center',
  padding: '0.5em',
  maxWidth: '50rem',
}));

const CustomCardHeader = styled(CardHeader)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));
const CustomListItemText = styled(ListItemText)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));
const CustomListItemIcon = styled(ListItemIcon)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));

const CustomTextField = styled(TextField)(({ theme }) => ({
  backgroundColor: theme.palette.surface.variant,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
  width: '75%'
}));

const AddButton = styled(Button)(({theme}) => ({
  width:'25%',
}));


class Forums extends Component {
  state = {
    input: '',
    forumsNames: ["New Forum1", "New Forum2", "New Forum3"]
  };
  render() {
    //States 
    const input = this.state.input;
    const setInput= (params) => this.setState({ input: params });
    const forumsNames = this.state.forumsNames;
    const setForumName= (params) => this.setState({ forumsNames: params });

    const addForum = () => {
      setForumName([...forumsNames, input]);
      setInput('');
    };

    function noInput(input) {
      if(input !== ''){
        return <AddButton variant='contained' color='success' onClick={addForum}>Create Forum</AddButton>
      }else{
        return <AddButton variant='outlined' color='success' disabled>Create Forum</AddButton>
      };
    };

    return (
      <><h1>Forums</h1>
      <StyledContainers>
        <CustomForumCard>
          <CustomCardHeader title='Create a New Forum'></CustomCardHeader>
          <CardContent>
            <Stack spacing={3} direction='row'>
              <CustomTextField variant='filled' label='Name for new forum' placeholder='New Forum' color='success' value={input} onChange={event => setInput(event.target.value)}></CustomTextField>
              {noInput(input)}
            </Stack>
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      <StyledContainers>
        <CustomForumCard>
          <CustomCardHeader title='Active Forums'></CustomCardHeader>
          <CardContent>
            <List>
              {forumsNames.map(forumName => (
                <ListItem>
                  <ListItemButton>
                    <CustomListItemIcon><Inbox/></CustomListItemIcon>
                    <CustomListItemText primary={forumName}/>
                    <CustomListItemIcon><Badge badgeContent={5} color='primary'><MessageOutlined/></Badge></CustomListItemIcon>
                  </ListItemButton>
                </ListItem>
              ))}
            </List>
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      </>
    );
  }
}

export default Forums;