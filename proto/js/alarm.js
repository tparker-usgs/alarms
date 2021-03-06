/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!


goog.provide('proto.gov.usgs.volcanoes.alarm.Alarm');
goog.provide('proto.gov.usgs.volcanoes.alarm.Alarm.State');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');


/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.gov.usgs.volcanoes.alarm.Alarm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.gov.usgs.volcanoes.alarm.Alarm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.gov.usgs.volcanoes.alarm.Alarm.displayName = 'proto.gov.usgs.volcanoes.alarm.Alarm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.toObject = function(opt_includeInstance) {
  return proto.gov.usgs.volcanoes.alarm.Alarm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.gov.usgs.volcanoes.alarm.Alarm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gov.usgs.volcanoes.alarm.Alarm.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getField(msg, 1),
    type: jspb.Message.getField(msg, 2),
    state: jspb.Message.getField(msg, 3),
    region: jspb.Message.getField(msg, 4),
    message: jspb.Message.getField(msg, 5),
    attachment: msg.getAttachment_asB64()
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.gov.usgs.volcanoes.alarm.Alarm}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.gov.usgs.volcanoes.alarm.Alarm;
  return proto.gov.usgs.volcanoes.alarm.Alarm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.gov.usgs.volcanoes.alarm.Alarm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.gov.usgs.volcanoes.alarm.Alarm}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setType(value);
      break;
    case 3:
      var value = /** @type {!proto.gov.usgs.volcanoes.alarm.Alarm.State} */ (reader.readEnum());
      msg.setState(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setRegion(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setMessage(value);
      break;
    case 6:
      var value = /** @type {!Uint8Array} */ (reader.readBytes());
      msg.setAttachment(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.gov.usgs.volcanoes.alarm.Alarm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.gov.usgs.volcanoes.alarm.Alarm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.gov.usgs.volcanoes.alarm.Alarm.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = /** @type {string} */ (jspb.Message.getField(message, 1));
  if (f != null) {
    writer.writeString(
      1,
      f
    );
  }
  f = /** @type {string} */ (jspb.Message.getField(message, 2));
  if (f != null) {
    writer.writeString(
      2,
      f
    );
  }
  f = /** @type {!proto.gov.usgs.volcanoes.alarm.Alarm.State} */ (jspb.Message.getField(message, 3));
  if (f != null) {
    writer.writeEnum(
      3,
      f
    );
  }
  f = /** @type {string} */ (jspb.Message.getField(message, 4));
  if (f != null) {
    writer.writeString(
      4,
      f
    );
  }
  f = /** @type {string} */ (jspb.Message.getField(message, 5));
  if (f != null) {
    writer.writeString(
      5,
      f
    );
  }
  f = /** @type {!(string|Uint8Array)} */ (jspb.Message.getField(message, 6));
  if (f != null) {
    writer.writeBytes(
      6,
      f
    );
  }
};


/**
 * @enum {number}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.State = {
  OK: 0,
  WARNING: 1,
  CRITICAL: 2,
  UNKNOWN: 3
};

/**
 * optional string name = 1;
 * @return {string}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/** @param {string} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setName = function(value) {
  jspb.Message.setField(this, 1, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearName = function() {
  jspb.Message.setField(this, 1, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasName = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional string type = 2;
 * @return {string}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getType = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/** @param {string} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setType = function(value) {
  jspb.Message.setField(this, 2, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearType = function() {
  jspb.Message.setField(this, 2, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasType = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional State state = 3;
 * @return {!proto.gov.usgs.volcanoes.alarm.Alarm.State}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getState = function() {
  return /** @type {!proto.gov.usgs.volcanoes.alarm.Alarm.State} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/** @param {!proto.gov.usgs.volcanoes.alarm.Alarm.State} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setState = function(value) {
  jspb.Message.setField(this, 3, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearState = function() {
  jspb.Message.setField(this, 3, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasState = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional string region = 4;
 * @return {string}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getRegion = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/** @param {string} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setRegion = function(value) {
  jspb.Message.setField(this, 4, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearRegion = function() {
  jspb.Message.setField(this, 4, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasRegion = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional string message = 5;
 * @return {string}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getMessage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/** @param {string} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setMessage = function(value) {
  jspb.Message.setField(this, 5, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearMessage = function() {
  jspb.Message.setField(this, 5, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasMessage = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional bytes attachment = 6;
 * @return {!(string|Uint8Array)}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getAttachment = function() {
  return /** @type {!(string|Uint8Array)} */ (jspb.Message.getFieldWithDefault(this, 6, ""));
};


/**
 * optional bytes attachment = 6;
 * This is a type-conversion wrapper around `getAttachment()`
 * @return {string}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getAttachment_asB64 = function() {
  return /** @type {string} */ (jspb.Message.bytesAsB64(
      this.getAttachment()));
};


/**
 * optional bytes attachment = 6;
 * Note that Uint8Array is not supported on all browsers.
 * @see http://caniuse.com/Uint8Array
 * This is a type-conversion wrapper around `getAttachment()`
 * @return {!Uint8Array}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.getAttachment_asU8 = function() {
  return /** @type {!Uint8Array} */ (jspb.Message.bytesAsU8(
      this.getAttachment()));
};


/** @param {!(string|Uint8Array)} value */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.setAttachment = function(value) {
  jspb.Message.setField(this, 6, value);
};


proto.gov.usgs.volcanoes.alarm.Alarm.prototype.clearAttachment = function() {
  jspb.Message.setField(this, 6, undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.gov.usgs.volcanoes.alarm.Alarm.prototype.hasAttachment = function() {
  return jspb.Message.getField(this, 6) != null;
};


