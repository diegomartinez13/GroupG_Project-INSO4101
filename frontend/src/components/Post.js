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
  const author = props.author;
  const post_id = props.post_id;
  const likes = props.likes;
  const dislikes = props.dislikes;

  const [comments, setComments] = useState([]);
  const URL_POST_COMMENTS = 'http://localhost:5000/comments/' + post_id;
  useEffect(() => {
    fetch(URL_POST_COMMENTS)
      .then(response => response.json())
      .then(data => setComments(data));
  }, []);

  return (
    <CustomAccordion>
      <CustomAccordionSummary expandIcon={<CustomExpand />}>
        <Stack direction="row" justifyContent="space-between" alignItems="center" spacing={3}>
        <CustomAccountCircle></CustomAccountCircle>
        <CustomTypo variant='h6'>"{title}"</CustomTypo>
        <CustomTypo variant='subtitle2'> by: {author}</CustomTypo>
        </Stack>
      </CustomAccordionSummary>
      <CustomAccordionDetails>
        <CustomTypo variant='body1'>{content}</CustomTypo>
        <CustomTypo variant='body2'> -- Created at: {date}</CustomTypo>
        <CustomTypo variant='body2'> -- Likes: {likes} Dislikes: {dislikes}</CustomTypo>
        <CustomTypo variant='body2'> -- Comments:</CustomTypo>
        {comments.map(comment => (
          <Post key={comment.post_id} post_id={comment.post_id} title={comment.title} content={comment.content} creation_date={comment.created_at} author={comment.username} likes={comment.likes} dislikes={comment.dislikes}/>
        ))}
      </CustomAccordionDetails>
    </CustomAccordion>
  );
}

export default Post;