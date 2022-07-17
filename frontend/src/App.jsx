import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import HomeScreen from './pages/HomeScreen';
import LoginScreen from './pages/LoginScreen';
import SignUpScreen from './pages/SignUpScreen';
import UserProfileScreen from './pages/UserProfileScreen';
import ContributorProfileScreen from './pages/ContributorProfileScreen';
import TeachUsScreen from './pages/TeachUsScreen';
import RecipeDetailsScreen from './pages/RecipeDetailsScreen';
import ModifyRecipes from './pages/ModifyRecipes';

const App = () => {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/register" element={<SignUpScreen />} />
          <Route path="/userProfile" element={<UserProfileScreen />} />
          <Route path="/contributorProfile" element={<ContributorProfileScreen />} />
          <Route path="/teachUs" element={<TeachUsScreen />} />
          <Route path="/recipeDetails" element={<RecipeDetailsScreen />} />
          <Route path="/recipe/add" element={<ModifyRecipes />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App;