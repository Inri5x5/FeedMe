import React from 'react'
import styles from './styles/Footer.module.css'

const Footer = () => {
  return (
    <div className={styles.wrapper}>
      <footer className={styles.footer}>
        <div className={styles.container}>
          <div className={styles.row}>
            <div className={styles.footer_col}>
              <h4>FeedMe!.Co</h4>
              <div className={styles.desc}>
                This is footer
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div> 
  )
}

export default Footer