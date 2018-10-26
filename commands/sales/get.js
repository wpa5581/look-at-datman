/**
 * @fileoverview Module handling the sale getting command.
 * @author Alvin Lin (axl1439)
 */

const display = require('../../lib/display')

exports.command = 'get'

exports.aliases = ['i', 'info']

exports.description = 'Info about a sale'

exports.handler = argv => {
  display.displaySales()
}
