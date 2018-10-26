/**
 * @fileoverview Module handling the dealer listing command.
 * @author Alvin Lin (axl1439)
 */

const display = require('../../lib/display')

exports.command = 'list'

exports.aliases = ['ls']

exports.description = 'List available dealers'

exports.handler = argv => {
  display.displayDealers()
}
