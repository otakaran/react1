import React from 'react'
import { Component } from 'react'
import Table from './Table'

class App extends Component {
    render() {
        const characters = [
            {
              name: 'Charlie',
              job: 'Janitor',
            },
            {
              name: 'Mac',
              job: 'Bouncer',
            },
            {
              name: 'Dee',
              job: 'Aspring actress',
            },
            {
              name: 'Dennis',
              job: 'Bartender',
            },
        ]

        return (
            <div className="App">
                    <h1>Hello, React!</h1>
                <div className="container">
                    <Table characterData={characters} />
                </div>
            </div>
      )
    }
  }

export default App