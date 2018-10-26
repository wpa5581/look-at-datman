/**
 * @fileoverview Module handling the dealer subcommands.
 * @author Alvin Lin (axl1439)
 */

exports.command = 'vehicle'

exports.aliases = ['vehicles']

exports.description = 'Manage vehicles in the database'

exports.builder = yargs => {
  yargs.commandDir('vehicles').demandCommand()
}
