import React, {Component} from 'react';
import {styled, Button, Container, TextField, Stack, Badge, Typography} from "@mui/material/"
import {Card, CardContent, CardHeader} from "@mui/material/"
import {Accordion, AccordionSummary, AccordionDetails} from "@mui/material/"
import { MessageOutlined} from '@mui/icons-material/';
import ForumChat from './ForumChat'

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
const CustomAccordion = styled(Accordion)(({ theme }) => ({
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

const CustomMessageIcon = styled(MessageOutlined)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));
const CustomAccordionSummary = styled(AccordionSummary)(({ theme }) => ({
  color: theme.palette.surface.text,
  '& .MuiAccordionSummary-expandIconWrapper.Mui-expanded':{transform: 'rotate(0deg)'}
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
      <>
      <StyledContainers>
        <h1>Forums</h1>
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
              {forumsNames.map(forumName => (
                <CustomAccordion>
                  <CustomAccordionSummary
                    expandIcon={<Badge badgeContent={5} color='primary'><CustomMessageIcon /></Badge>}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                    >
                    <Typography variant='body1'>{forumName}</Typography>
                  </CustomAccordionSummary>
                  <AccordionDetails>
                    <Typography variant='body2'> TEST </Typography>
                    <ForumChat></ForumChat>
                  </AccordionDetails>
                </CustomAccordion>
              ))}
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      </>
    );
  }
}

export default Forums;