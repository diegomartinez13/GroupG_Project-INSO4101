import {React, useState, useEffect} from 'react';
import { styled, Typography} from '@mui/material';
import { Accordion, AccordionSummary, AccordionDetails, Stack} from '@mui/material';
import { AccountCircle } from '@mui/icons-material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

const CustomAccordion = styled(Accordion)(({ theme }) => ({
  backgroundColor: theme.palette.surface.main,
  color: theme.palette.surface.text,
  '& .rbc-event': {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.text,
  },
}));
const CustomAccordionSummary = styled(AccordionSummary)(({ theme }) => ({
  color: theme.palette.surface.text,
}));

const CustomAccordionDetails = styled(AccordionDetails)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));
const CustomTypo = styled(Typography)(({ theme }) => ({
  color: theme.palette.surface.text,
}
));

const CustomAccountCircle = styled(AccountCircle)(({ theme }) => ({
  color: theme.palette.surface.text,
}));

const CustomExpand = styled(ExpandMoreIcon)(({ theme }) => ({
  color: theme.palette.surface.text,
}));

function Post(props) {
  const title = props.title;
  const content = props.content;
  const date = props.creation_date;
  const author_id = props.author;
  const parent_post_id = props.parent_post_id;

  const [authorUsername, setAuthorUsername] = useState([]);
  const URL_USERNAME = 'http://localhost:5000/user/username/' + author_id;
  const [parentPost, setParentPost] = useState([]);
  const URL_POST_TITLE = 'http://localhost:5000/tittle/' + parent_post_id;
  useEffect(() => {
    fetch(URL_USERNAME)
      .then(response => response.json())
      .then(data => setAuthorUsername(data.username));
    fetch(URL_POST_TITLE)
      .then(response => response.json())
      .then(data => setParentPost(data.title));
    console.log(parentPost)
  }, []);

  function ifParentPost() {
    if (parent_post_id == null || parent_post_id == 0 || parent_post_id == '' || parent_post_id == -1) {
      return null;
    } else {
      return (
        <CustomTypo variant='body2'> -- Parent post: {parentPost}</CustomTypo>
      );
    }
  };

  return (
    <CustomAccordion>
      <CustomAccordionSummary expandIcon={<CustomExpand />}>
        <Stack direction="row" justifyContent="space-between" alignItems="center" spacing={3}>
        <CustomAccountCircle></CustomAccountCircle>
        <CustomTypo variant='h6'>"{title}"</CustomTypo>
        <CustomTypo variant='subtitle2'> by: {authorUsername}</CustomTypo>
        </Stack>
      </CustomAccordionSummary>
      <CustomAccordionDetails>
        <CustomTypo variant='body1'>{content}</CustomTypo>
        <CustomTypo variant='body2'> -- Created at: {date}</CustomTypo>
        {ifParentPost()}
      </CustomAccordionDetails>
    </CustomAccordion>
  );
}

export default Post;