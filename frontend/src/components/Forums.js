import {React, useState, useEffect} from 'react';
import {styled, Container} from "@mui/material/"
import {Card, CardContent, CardHeader, Stack, Button} from "@mui/material/"
import PostList from './PostList';
import NewPost from './NewPost';


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

function Forums() {
  const [userLoggedIn, setUserLoggedIn] = useState(sessionStorage.getItem('user') != null && sessionStorage.getItem('user') != undefined && sessionStorage.getItem('user') != 'undefined')

  // TODO: Add a check to see if the user is logged in or not to comment on posts
  // TODO: Add comment fuctionality to posts
  function isLoggedToPost(){
    if (!userLoggedIn) {
      return <>
      <StyledContainers>
        <CustomForumCard>
          <CustomCardHeader title='Please Login to Add New Posts'></CustomCardHeader>
          <CardContent>
            <Stack direction='row' justifyContent="space-evenly" alignContent='center' spacing={2}>
              <Button variant="contained" href="/login">LOG-IN</Button>
              <Button variant="contained" href="/signup">REGISTER NOW!</Button>
            </Stack>
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      </>
    } else {
      return <>
      <StyledContainers>
        <CustomForumCard>
          <CustomCardHeader title='Add New Post'></CustomCardHeader>
          <CardContent>
            <NewPost />
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      </>
    };
  };
    return (
      <>
      
      <StyledContainers>
        <h1>Forum</h1>
        
        <CustomForumCard>
          
          <CustomCardHeader title='Posts'></CustomCardHeader>
          <CardContent>
            <PostList />
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      {isLoggedToPost()}
      
      </>
    );
}


export default Forums;