/**
*******************************************************************************
* @file                  SMacHsTtiTraceBitField.h
* @version               wn9.0
* @date                  04-OCT-2013 07:01:25
* @author                uselvara
* @brief                 SBitField: Machs TTI Trace Structure
*
* Item Specification
*
* Status
*
* Original author
*
* Copyright (c) Nokia 2005. All rights reserved.
*******************************************************************************/
#ifndef _SMACHS_TTITRACE_BITFIELD_H
#define _SMACHS_TTITRACE_BITFIELD_H

#ifdef PLATFORM_DEVICE_FARADAY
#include <STtiTraceCommonHeader.h>
#else
#include <SMacHsTtiTraceCommonHeader.h>
#endif

#include <EMacHsRankInfo.h>
#include <EHsDpcchAckNack.h>
#include <EMachsTtiTracePrioQType.h>
#include <EMachsTtiTraceTransmissionType.h>
#include <EMachsTtiTraceModulationType.h>

struct SMacHsTtiTraceBitFieldForCellInfo
{
    u32    cellID               :16;    /* word 1 */
    u32    nbrofAgguser         : 9;
    u32    nbrofProposedLocalUser   : 3;
    u32    MoCNTrigger          : 1;  /* 0: MoCN disable, 1: MoCN enable */
    u32    pading2              : 3;
    u32    nbrofSchAggUser      : 3;  /* HS-SCCH code number >= 4 *//* word 2 */
    u32    transCarrierPower    :17;  /* Unit: mW */
    u32    discardedCodes       : 4;  /* HS-DPSCH code number >= 15 */
    u32    nbrofLocalUser       : 8;
    u32    nbrofLocalU      : 9;        /* primary carrier in local machs *//* word 3 */
    u32    k                : 9;
    u32    nbrOfBannedUsers : 9;
    u32    nbrofReceiveAggUser  : 4;
    u32    calibrationOngoing  : 1;    
    u32    availPdschPower      :16;  /* Unit: dBm */  /* word 4 */
    u32    maxUsablePower       :16;  /* Unit: dBm */ 
    u32    nonHSDPAPower        :16;    /* word 5 */
    u32    nbrofLocalUOp1       :8;
    u32    nbrofLocalUOp2       :8;
    u32    nbrofLocalUOp3       :8;  /*word 6 */
    u32    nbrofLocalUOp4       :8;
    u32    phaseOffset          :9;
    u32    pading6              :7;   /* 6*3=18 */
    /* could not add any new word. If needed, please also check struct SBrowserMacHsTtiTrace */
};
typedef struct SMacHsTtiTraceBitFieldForCellInfo SMacHsTtiTraceBitFieldForCellInfo;

struct SMacHsTtiTraceBitFieldForCore
{
    /* ACKNACK meanings:
    typedef    enum EHsDpcchAckNack{
        EHsDpcchAckNack_Dtx              = 0,
        EHsDpcchAckNack_UlCmGap          = 1,
        EHsDpcchAckNack_AckDtx           = 2,
        EHsDpcchAckNack_Ack              = 3,
        EHsDpcchAckNack_NackDtx          = 4,
        EHsDpcchAckNack_Nack             = 5,
        EHsDpcchAckNack_None             = 6,
        EHsDpcchAckNack_NoValue          = 7,
        EHsDpcchAckNack_NoSchedulingInfo = 8
    } EHsDpcchAckNack; */
    u32    ackNack_u1s1         : 4;   /* word 1 */
    u32    ackNack_u2s1         : 4;
    u32    ackNack_u3s1         : 4;
    u32    ackNack_u4s1         : 4;    
    u32    ackNack_u5s1         : 4;
    u32    ackNack_u6s1         : 4;
    u32    ackNack_u7s1         : 4;
    u32    ackNack_u8s1         : 4;
    u32    ackNack_u9s1         : 4;    /* word 2 */
    u32    ackNack_u10s1        : 4;
    u32    ackNack_u11s1        : 4;    
    u32    ackNack_u12s1        : 4;
    u32    ackNack_u13s1        : 4;
    u32    ackNack_u14s1        : 4;
    u32    ackNack_u15s1        : 4;
    u32    ackNack_u16s1        : 4;
    u32    ackNack_u17s1        : 4;    /* word 3 */
    u32    ackNack_u18s1        : 4;
    u32    ackNack_u19s1        : 4;
    u32    ackNack_u20s1        : 4;
    u32    ackNack_u21s1        : 4;
    u32    ackNack_u22s1        : 4;
    u32    ackNack_u23s1        : 4;
    u32    ackNack_u24s1        : 4;
    u32    ackNack_u1s2         : 4;    /* word 4 */
    u32    ackNack_u2s2         : 4;
    u32    ackNack_u3s2         : 4;
    u32    ackNack_u4s2         : 4;
    u32    ackNack_u5s2         : 4;
    u32    ackNack_u6s2         : 4;
    u32    ackNack_u7s2         : 4;    
    u32    ackNack_u8s2         : 4;
    u32    ackNack_u9s2         : 4;    /* word 5 */
    u32    ackNack_u10s2        : 4;    
    u32    ackNack_u11s2        : 4;
    u32    ackNack_u12s2        : 4;
    u32    ackNack_u13s2        : 4;
    u32    ackNack_u14s2        : 4;
    u32    ackNack_u15s2        : 4;
    u32    ackNack_u16s2        : 4;
    u32    ackNack_u17s2        : 4;    /* word 6 */
    u32    ackNack_u18s2        : 4;
    u32    ackNack_u19s2        : 4;
    u32    ackNack_u20s2        : 4;
    u32    ackNack_u21s2        : 4;
    u32    ackNack_u22s2        : 4;
    u32    ackNack_u23s2        : 4;
    u32    ackNack_u24s2        : 4;
    u32    ackNack_u1s1Rep2     : 4;    /* word 7 */ 
    u32    ackNack_u2s1Rep2     : 4;
    u32    ackNack_u3s1Rep2     : 4;
    u32    ackNack_u4s1Rep2     : 4;   
    u32    ackNack_u5s1Rep2     : 4;   
    u32    ackNack_u6s1Rep2     : 4;
    u32    ackNack_u7s1Rep2     : 4;
    u32    ackNack_u8s1Rep2     : 4;
    u32    ackNack_u9s1Rep2     : 4;    /* word 8 */
    u32    ackNack_u10s1Rep2    : 4;
    u32    ackNack_u11s1Rep2    : 4;    
    u32    ackNack_u12s1Rep2    : 4;
    u32    ackNack_u13s1Rep2    : 4;
    u32    ackNack_u14s1Rep2    : 4;
    u32    ackNack_u15s1Rep2    : 4;
    u32    ackNack_u16s1Rep2    : 4;
    u32    ackNack_u17s1Rep2    : 4;    /* word 9 */
    u32    ackNack_u18s1Rep2    : 4;
    u32    ackNack_u19s1Rep2    : 4;
    u32    ackNack_u20s1Rep2    : 4;
    u32    ackNack_u21s1Rep2    : 4;
    u32    ackNack_u22s1Rep2    : 4;
    u32    ackNack_u23s1Rep2    : 4;
    u32    ackNack_u24s1Rep2    : 4;
    u32    ackNack_u1s2Rep2     : 4;    /* word 10 */
    u32    ackNack_u2s2Rep2     : 4;
    u32    ackNack_u3s2Rep2     : 4;
    u32    ackNack_u4s2Rep2     : 4;
    u32    ackNack_u5s2Rep2     : 4;
    u32    ackNack_u6s2Rep2     : 4;
    u32    ackNack_u7s2Rep2     : 4;
    u32    ackNack_u8s2Rep2     : 4;
    u32    ackNack_u9s2Rep2     : 4;    /* word 11 */
    u32    ackNack_u10s2Rep2    : 4;    
    u32    ackNack_u11s2Rep2    : 4;
    u32    ackNack_u12s2Rep2    : 4;
    u32    ackNack_u13s2Rep2    : 4;
    u32    ackNack_u14s2Rep2    : 4;
    u32    ackNack_u15s2Rep2    : 4;
    u32    ackNack_u16s2Rep2    : 4;
    u32    ackNack_u17s2Rep2    : 4;    /* word 12 */
    u32    ackNack_u18s2Rep2    : 4; 
    u32    ackNack_u19s2Rep2    : 4;
    u32    ackNack_u20s2Rep2    : 4;
    u32    ackNack_u21s2Rep2    : 4;
    u32    ackNack_u22s2Rep2    : 4;
    u32    ackNack_u23s2Rep2    : 4;
    u32    ackNack_u24s2Rep2    : 4;
    u32    usedSchedAlg         : 2;    /* word 13*//* 0: RRFixed, 1: PFRFixed, 2: RRFloat, 3: PFRFloat*/  /* word 7 */
    u32    cpuLoad              : 7;
    u32    nbrOfHarqs           :10;
    u32    pading3              :13;
    u32    coreid               :32;    /* word 14*/

};
typedef struct SMacHsTtiTraceBitFieldForCore SMacHsTtiTraceBitFieldForCore;

struct SMacHsTtiTraceBitFieldForCell
{
    struct SMacHsTtiTraceBitFieldForCellInfo cell[3];
};
typedef struct SMacHsTtiTraceBitFieldForCell SMacHsTtiTraceBitFieldForCell;

struct SMacHsTtiTraceBitFieldForLocalUser
{       
    u32     ueCategory                                      : 5;    /* word 1 */
    u32     nbrOfPdschCodes                                 : 4;
    u32     lchId                                           :16;
    u32     SI                                              : 2;
    u32     modulation                                      : 2;
    u32     operatorID                                      : 3;    /* 0: invalid, 1-5, 7: 254 */
    u32     userId                                          :16;  // nbccid for hsdpa user.     /* word 2 */
    u32     rnti                                            :16;  // h-rnti
    u32     cellId                                          :16;    /* word 3 */
    u32     spiWeight                                       : 8;
    u32     edrxEnable                                      : 1;    // 0: disable, 1: enable
    u32     averageCodeRate                                 : 7;    // (0-100)
    u32     internalPrioQId                                     : 9; /* if prioQType == DRB, it must be less than 486 */ /* word 4 */
    u32     tsn                                             :14;    
    u32     pdschPowerIndex                                 : 9;
    u32     t1Tsn                                           :14;    /* word 5 */
    u32     harqIndex                                       : 4;
    u32     windowSize                                      : 8;
    u32     compensatedCqi                                  : 6;
    u32     recommendedTbs                                  :16;    /* word 6 */
    u32     finalTbs                                        :16;
    u32     scchPower                                       :16;    /* word 7 */
    u32     pdschPower                                      :16;
    u32     a                                               :15;    /* word 8 */
    u32     bufferOccupancyInBits                           :15;
    u32     pciValue                                        : 2;
    u32     tpInBitsPerTTI                                      :19;    /* word 9 */
    u32     cqi                                             : 6;
    u32     nbrOfMacDPdusInTb                               : 7;
    u32     akNkReptFactor                                  : 2;    /* word 10 */
    u32     averageCqi                                      : 7;
    u32     ndi                                             : 1;
    u32     transmissionNbr                                 : 3;
    u32     carrierStreamIndex                              : 3;
    u32     rv                                              : 3;
    u32     spi                                             : 4; 
    u32     pading4                                         : 9;
    u32     scalingFactorQos                                :32;    /* word 11 */
    u32     activityFactor                                  :32;    /* word 12 */
    u32     MaxPowerWithSharedRes                           :16;    /* word 13 */
    u32     neededPowerWithSharedResShared                  :16;
    u32     maxAllowedTBSWithSharedRes                      :16;    /* word 14 */
    u32     maxCRLimitedBlockSize                           :16;
    u32     paddingBits                                     :16;    /* word 15 */
    u32     cqiVariance                                     :10;
    u32     codeMuxIndex                                    : 5;    //(0-4*6, 0: means codeMuxEnable = 0)
    u32     mimoModeInd                                     : 1;
    u32     neededCodes                                     : 4;    /* word 16 */
    u32     maxNeededCodes                                  : 4;
    u32     spiChangeIndication                             : 2;
    u32     prioQType                                       : 2; /* 0: DRB, 1: SRB, 2: voice */
    u32     pdschCodeOffset                                 : 4; /* pdsch start code */
    u32     scchCode                                        : 7;
    u32     pading7                                         : 9;
    /* machsAddress: 
        when traceType == 3(local user scheduling info, like SC user, primary carrier of MC user), local machs address; 
        when traceType == 4(secondary carrier scheduling info of aggregated user, and secondary carrier is set up in remote machs), remote machs address;
        when traceType == 5(secondary carrier scheduling info of aggregated user, but the primary carrier is not set up in local machs),remote machs address. 
    */    
    u32     sumSPIWeight                                    :16; /*word 17*/
    u32     machsAddress                                    :16;
    u32     excessRes                                       :32; /*word 18*/ 
    /* could not add any new word. If needed, please also check struct SBrowserMacHsTtiTrace */
};
typedef struct SMacHsTtiTraceBitFieldForLocalUser SMacHsTtiTraceBitFieldForLocalUser;

union SMacTtiTrace
{
    struct SMacHsTtiTraceBitFieldForCore        machsCore;  /* 14 words */
    struct SMacHsTtiTraceBitFieldForCell        machsCell;  /*  3*6 = 18 words */
    struct SMacHsTtiTraceBitFieldForLocalUser   machsSchUser;   /* 18 words */
};
typedef union SMacTtiTrace SMacTtiTrace;

enum EMacHs_TraceType
{
    /* core trace */
    EMacHs_TraceType_CoreTrace  = 0,        /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForCore) =!*/
    /* local cell trace */
    EMacHs_TraceType_LocalCellTrace = 1,    /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForCell) =!*/
    /* mapping cell trace */
    EMacHs_TraceType_MappingCellTrace = 2,  /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForCell) =!*/
    /* local user trace or primary carrier trace of CA user */
    EMacHs_TraceType_LocalUserTrace = 3,    /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForLocalUser) =!*/
    /* Seconary carrier trace of CA user, but the secondary carrier is set up in remote machs */
    EMacHs_TraceType_CAUserTrace_ForSecondCarrierOnRemote = 4,  /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForLocalUser) =!*/
    /* Seconary carrier trace of CA user, but primary carrier is set up in remote machs */
    EMacHs_TraceType_CAUserTrace_ForPrimaryCarrierOnRemote = 5 /*!= INTERPRET_DYNAMIC(SMacHsTtiTraceBitFieldForLocalUser) =!*/  
};
typedef enum EMacHs_TraceType EMacHs_TraceType;

struct SMacHsTtiTraceCommon
{
    u32                     traceType       : 3;    /*!= INTERPRET_BY_ENUM(EMacHs_TraceType) =!*/
    u32                     hour            : 5;    
    u32                     minute          : 6;
    u32                     second          : 6;
    u32                     millisecond     :10;
    u32                     pading1         : 2;
    u32     sfn                 :12;    /* word 2 */
    u32     subFrameNbr         : 4;
    u32     chipNbr             :12;
    u32     slotNbr             : 4;
    u32                     sequenceNo; /* word 3 */
};
typedef struct SMacHsTtiTraceCommon SMacHsTtiTraceCommon;

struct SMacHsTtiTraceBitField
{
    SMacHsTtiTraceCommon    ttiTraceCommon;
    union SMacTtiTrace      ttiTraceInfo;   
    /* 
        if traceType == 0: ttiTraceInfo.machsCore is valid;
        if traceType == 1/2: ttiTraceInfo.machsCell is valid;
        if traceType == 3/4/5: ttiTraceInfo.machsSchUser is valid. 
    */
};
typedef struct SMacHsTtiTraceBitField SMacHsTtiTraceBitField;

/* Notes on the above SMacHsTtiTraceBitField
 * ----------------------------
 * receivedAkNkCmux<n> - Several AckNack's exist because of repetition factor
 * and code multiplexing. Two consecutive ones has different repetition factor.
 * There are three groups of these, for each multiplexed user.
 *
 * Increment MACHS_TTI_TRACE_FIELD_VERSION by 1 in BrowserMacHsTtiTrace.c when
 * SMacHsTtiTraceBitField is updated
 */
#endif /* _SMACHS_TTITRACE_BITFIELD_H */

/**
*******************************************************************************
* @struct SMacHsTtiTraceBitField
* Development Workset :
*
* Design Part         :
*
* Description : This structure contains Machs TTI Trace Fields
*
* Reference           :
*
* @param
*                                                                   *
*
* Additional Information: -
* Definition Provided by   :
*
* Remember to put an empty line in the end of each definition file.
* Otherwise the compiler will generate a warning.
**********************************************************************/
