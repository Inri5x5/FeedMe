import React from 'react'
import ContributorRecipeCard from './ContributorRecipeCard'

const PublishedRecipeContainer = () => {
  return (
    <div style={{
        position: 'relative',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-start',
        alignItems:'center',
        marginTop: '20px',
        marginLeft: '20px',
        width: '88%'
      }}>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
        <ContributorRecipeCard></ContributorRecipeCard>
      </div>
  )
}

export default PublishedRecipeContainer