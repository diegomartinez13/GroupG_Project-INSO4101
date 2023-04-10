import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SideNavigation from './components/SideNavigation';
import HomePage from './pages/HomePage';
import EventsPage from './pages/EventsPage';
import RecyclingCentersPage from './pages/RecyclingCentersPage';
import ProfilePage from './pages/ProfilePage';
import ForumPage from './pages/ForumPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';

import { createTheme, ThemeProvider, useMediaQuery } from '@mui/material';
import ThemeToggle from './components/ThemeToggle';
import { Typography, Box, Container } from '@mui/material';
import logo from './assets/logo.jpg';
import { styled } from '@mui/material';

const light_theme = createTheme({
  palette: {
    primary: {
      main: '#2c6b28',
      onPrimary: '#ffffff',
      onPrimaryText: '#2c6b28',
      container: {
        main: '#aef4a0',
        text: '#002201',
        onContainer: '#002201',
        onContainerText: '#aef4a0',
      },
    },
    secondary: {
      main: '#53634e',
      onSecondary: '#ffffff',
      onSecondaryText: '#53634e',
      container: {
        main: '#d6e8cd',
        text: '#111f0f',
        onContainer: '#111f0f',
        onContainerText: '#d6e8cd',
      },
    },
    tertiary: {
      main: '#386569',
      onTertiary: '#ffffff',
      onTertiaryText: '#386569',
      container: {
        main: '#bcebef',
        text: '#002022',
        onContainer: '#002022',
        onContainerText: '#bcebef',
      },
    },
    error: {
      main: '#ba1a1a',
      onError: '#ffffff',
      onErrorText: '#BA1A1A',
      container: {
        main: '#ffdad6',
        text: '#410002',
        onContainer: '#410002',
        onContainerText: '#ffdad6',
      },
    },
    background: {
      default: '#fcfdf6',
      text: '#1a1c19',
      onBackground: '#1a1c19',
      onBackgroundText: '#fcfdf6',

    },
    outline: {
      main: '#73796e',
      text: '#fcfdf6',
    },
    surface: {
      main: '#fcfdf6',
      text: '#1a1c19',
      onSurface: '#1a1c19',
      onSurfaceText: '#fcfdf6',
      variant: '#dfe4d8',
      variantText: '#42493f',
      onVariant: '#42493f',
      onVariantText: '#dfe4d8',
    }
  },
});

const dark_theme = createTheme({
  palette: {
    primary: {
      main: '#93d786',
      text: '#003a04',
      onPrimary: '#003a04',
      onPrimaryText: '#93d786',
      container: {
        main: '#115211',
        text: '#aef4a0',
        onContainer: '#aef4a0',
        onContainerText: '#115211',
      },
    },
    secondary: {
      main: '#baccb2',
      text: '#263422',
      onSecondary: '#263422',
      onSecondaryText: '#baccb2',
      container: {
        main: '#3c4b37',
        text: '#d6e8cd',
        onContainer: '#d6e8cd',
        onContainerText: '#3c4b37',
      },
    },
    tertiary: {
      main: '#a0cfd3',
      text: '#00363a',
      onTertiary: '#00363a',
      onTertiaryText: '#a0cfd3',
      container: {
        main: '#1e4d51',
        text: '#bcebef',
        onContainer: '#bcebef',
        onContainerText: '#1e4d51',
      },
    },
    error: {
      main: '#ffb4ab',
      text: '#690005',
      onError: '#690005',
      onErrorText: '#ffb4ab',
      container: {
        main: '#93000a',
        text: '#ffdad6',
        onContainer: '#ffdad6',
        onContainerText: '#93000a',
      },
    },
    background: {
      default: '#1a1c19',
      text: '#e2e3dd',
      onBackground: '#e2e3dd',
      onBackgroundText: '#1a1c19',

    },
    outline: {
      main: '#8c9388',
      text: '1a1c19',
    },
    surface: {
      main: '#1a1c19',
      text: '#e2e3dd',
      onSurface: '#e2e3dd',
      onSurfaceText: '#1a1c19',
      variant: '#42493f',
      variantText: '#c2c8bc',
      onVariant: '#c2c8bc',
      onVariantText: '#42493f',
    }
  },
});



function App() {
  const [isOpen, setIsOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const isSmallScreen = useMediaQuery('(max-width: 600px)');

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const PageTitle = styled(Typography)(({ theme }) => ({
    color: theme.palette.surface.text,
  }
  ));

  return (
    <Box sx={{ backgroundColor: darkMode ? dark_theme.palette.background.default : light_theme.palette.background.default }}>
      <ThemeProvider theme={darkMode ? dark_theme : light_theme}>
        <BrowserRouter>
          <Container maxWidth="xl" sx={{ padding: 0 }}>
            <Box sx={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
              <Box sx={{ display: 'flex', flexGrow: 1 }}>
                  <Box sx={{ width: isSmallScreen? 0:'8em' }}>
                    <SideNavigation onToggleMenu={toggleMenu} />
                  </Box>
                <Box sx={{ flexGrow: 1 }}>
                  <Box sx={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                    <img src={logo} alt="MASTIETEC logo" width="50" height="50" style={{ margin: '1rem', borderRadius: '4rem'}}/>
                    <PageTitle variant="h6" sx={{ flexGrow: 1 }}>
                      Education Recycling Platform
                    </PageTitle>
                  </Box>
                  <ThemeToggle onToggleDarkMode={toggleDarkMode} themeType={darkMode} />
                  <Box sx={{ p: 2 }}>
                    <Routes>
                      <Route path="/" element={<HomePage />} />
                      <Route path="/events" element={<EventsPage />} />
                      <Route path="/recycling-centers" element={<RecyclingCentersPage />} />
                      <Route path="/profile" element={<ProfilePage />} />
                      <Route path="/forum" element={<ForumPage />} />
                      <Route path="/login" element={<LoginPage />} />
                      <Route path="/signup" element={<SignUpPage />} />

                    </Routes>
                  </Box>
                </Box>
              </Box>
            </Box>
          </Container>
        </BrowserRouter>
      </ThemeProvider>
    </Box>
  );
}

export default App;