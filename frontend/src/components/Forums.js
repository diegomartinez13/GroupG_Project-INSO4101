import React from 'react';
import {styled, Container, Typography} from "@mui/material/"
import {Card, CardContent, CardHeader} from "@mui/material/"
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
      <StyledContainers>
        <CustomForumCard>
          <CustomCardHeader title='Add New Post'></CustomCardHeader>
          <CardContent>
            <NewPost />
          </CardContent>
        </CustomForumCard>
      </StyledContainers>
      </>
    );
}


export default Forums;