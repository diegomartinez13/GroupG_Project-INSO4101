import { Card, CardMedia, CardContent, Typography, CardHeader, Grid } from '@mui/material';
import recyclingInfo from '../assets/recycling-info.jpg';
import sortingMaterials from '../assets/sorting-materials.jpg';
import recyclableMaterials from '../assets/recyclable-materials.jpg';
import { styled } from '@mui/material';





const HomePage = () => {
  const InfoCard = styled(Card)(({ theme }) => ({
    backgroundColor: theme.palette.surface.variant,
    alignContent: 'center',
    justifyContent: 'center',
    padding: '0.5em',
    margin: '0.5em',
    maxWidth: '50rem',
    '&:hover': {
      backgroundColor: theme.palette.secondary.container.main,
    },
  }
  ));

  const InfoCardTypography = styled(Typography)(({ theme }) => ({
    color: theme.palette.surface.text,
  }
  ));

  const InfoCardHeader = styled(CardHeader)(({ theme }) => ({
    color: theme.palette.surface.text,
  }
  ));
  return (
    <>
    <Grid container spacing={2} justifyContent="center" sx ={{ mt : 8}}>
      <InfoCard >
        <CardMedia
          component="img"
          height="200"
          src={recyclingInfo}
          alt="Recycling Information"
          draggable="false"
          sx={{
            objectFit: 'cover',
            objectPosition: 'center',
            borderRadius: '10px',
            paddungTop: '0.5em',
          }}
        />
        <InfoCardHeader title="Recycling Information" />
        <CardContent>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
            Recycling is the process of converting waste materials into new materials and objects.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
            Recycling can reduce the consumption of fresh raw materials, reduce energy usage, and reduce air and water pollution.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
            Recycling can also create jobs and stimulate the development of greener technologies.
          </InfoCardTypography>
        </CardContent>
      </InfoCard>

      <InfoCard >
        <CardMedia
          component="img"
          height="200"
          image={sortingMaterials}
          alt="Sorting Materials"
          draggable="false"
          sx={{
            objectFit: 'cover',
            objectPosition: 'center',
            borderRadius: '10px',
            paddungTop: '0.5em',
          }}
        />
        <InfoCardHeader title="How to properly sort and prepare materials for recycling" />
        <CardContent>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          To properly sort and prepare materials for recycling, start by checking with your local recycling program to see what can be recycled in your area.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          Rinse out any food or drink containers and remove any caps or lids before recycling.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          Flatten cardboard boxes and break down other large items to save space in your recycling bin.
          </InfoCardTypography>
        </CardContent>
      </InfoCard>

      <InfoCard>
        <CardMedia
          component="img"
          height="200"
          image={recyclableMaterials}
          alt="Types of Recyclable Materials"
          draggable="false"
          sx={{
            objectFit: 'cover',
            objectPosition: 'center',
            borderRadius: '10px',
            paddungTop: '0.5em',
          }}
        />
        <InfoCardHeader title=" Types of materials that can and cannot be recycled" />
        <CardContent>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          Materials that can typically be recycled include paper, cardboard, glass, metal, and certain types of plastic.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          Materials that typically cannot be recycled include plastic bags, styrofoam, and certain types of plastic, such as plastic wrap and plastic utensils.
          </InfoCardTypography>
          <InfoCardTypography variant="body1" color="textSecondary" component="p">
          When in doubt, check with your local recycling program to see what materials can be recycled in your area.
          </InfoCardTypography>
        </CardContent>
      </InfoCard>
    </Grid>
    </>
  );
};

export default HomePage;