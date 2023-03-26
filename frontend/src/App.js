import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import HomePage from './pages/HomePage';
import EventsPage from './pages/EventsPage';
import RecyclingCentersPage from './pages/RecyclingCentersPage';
import ProfilePage from './pages/ProfilePage';
import ForumPage from './pages/ForumPage';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/events" element={<EventsPage />} />
        <Route path="/recycling-centers" element={<RecyclingCentersPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/forum" element={<ForumPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;